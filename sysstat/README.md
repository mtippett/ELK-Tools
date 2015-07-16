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
on a single line and 


##


