# sysstat

The sysstat package is a suite that has lineage going back to big-iron Unixen provides system metrics that allows 
historic analysis of

sysstat's workhorse is the sar tool.   This generates human readable, but not necessarily machine parseable output.
Fortunately, sadf has been added to the package that allows machine readable in multiple ways.

## Theory of Operation

Based on the previous interactions with logstash and kibana, it is generally easier to iterate with a front-end tool getting the data into 
a reasonable form.  This allows morphing of the raw output to something that is a bit better tuned for the way that Logstash and Elasticsearch
operate.

The sadf output would need to be modified to provide a per-system/per-metric input to elastic search.  Fortunately, logstash likes json 
on a single line and this makes it easy to parse.  So a pipeline similar to the following would be needed.

  <sar in json> | <tweak the data, split into transactions> | <logstash> | <elastic search>

## Activities in each step of the pipeline

### sar in json

Fortunately, sadf makes this very easy.  The sadf when invoked as follows

  sadf -j --  -A

gives output similar 

  { "sysstat": 
    {
      "sysdata-version": 2.13,
      "hosts": [
      {
        "nodename": "rasp01",
        "sysname": "Linux",
        "release": "3.18.11-v7+",
        "machine": "armv7l",
        "number-of-cpus": 4,
        "file-date": "2015-07-16",
        "statistics": [
          {
             "timestamp": {"date": "2015-07-16", "time": "07:00:01", "utc": 1, "interval": 184467440737095516},
             "paging": {"pgpgin": 0.00, "pgpgout": 0.00, "fault": 0.00, "majflt": 0.00, "pgfree": 0.00, "pgscank": 0.00, "pgscand": 0.00, "pgsteal": 0.00, "vmeff-percent": 0.00},
             
              <other statistics>
          }
      }
    }    
  }


