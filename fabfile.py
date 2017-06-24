from fabric.api import local

def test():
    clean()
    local('py.test tests/*.py -s -v')

def clean():
    local('rm data/check_wsir_recs.out')
    local('rm data/lab_wsir_update_records.csv')

def package():
    local('echo "RPM or tarball")

def build():
    test()
    package()
