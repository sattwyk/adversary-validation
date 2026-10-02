# Patches

upstream-divergent-log-test.patch copies only the fixing commit's regression test onto the parent. It constructs divergent log images and therefore belongs exclusively to reproduction/baseline preparation. Hashes and exact Git postimages are in benchmark.json; original MIT/Apache licensing is retained alongside it. No Raft algorithm is modified. The early election failure observed locally remains inconclusive about the documented replication mechanism.
