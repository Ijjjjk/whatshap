"""
Tests for whatshap extend module

"""

from whatshap.cli.haplotagphase import run_haplotagphase


def test_extend():
    run_haplotagphase(
        variant_file="tests/data/pacbio/variants.vcf",
        alignment_file="tests/data/pacbio/haplotagged.bam",
        reference="tests/data/pacbio/reference.fasta",
        output="/dev/null",
    )
