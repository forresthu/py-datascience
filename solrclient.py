from SolrClient import SolrClient

solr = SolrClient('http://localhost:8983/solr')
res = solr.query('dev', {
    'q': 'test'
})
