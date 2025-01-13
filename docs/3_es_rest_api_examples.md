# FTS and Interval Query

_Full Text Search (FTS)_ is a feature in databases that allows searching and matching of text documents based on __relevance and ranking__. It is commonly used in applications such as search engines, content management systems, and data analytics.

An _Interval Query_ is a query that __retrieves data based on overlapping or intersecting intervals__. It is commonly used in applications where data is organized into time intervals, such as scheduling, event management, and time-series data analysis.

Interval Query example:

```
POST _search
{
  "query": {
    "intervals" : {
      "my_text" : {  // match field my_text
        "all_of" : {  // any of the following intervals
          "ordered" : true,  // the two intervals has a order
          "intervals" : [
            {
              "match" : {
                "query" : "my favorite food",
                "max_gaps" : 0,  // no gap between terms
                "ordered" : true  // terms need to be in this order
              }
            },
            {
              "any_of" : {
                "intervals" : [
                  { "match" : { "query" : "hot water" } },
                  { "match" : { "query" : "cold porridge" } }
                ]
              }
            }
          ]
        }
      }
    }
  }
}
```

