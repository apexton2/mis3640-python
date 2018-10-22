def sed(pattern, replace, source, dest):
    """"""
    f_source = open(source, 'r')
    f_dest = open(dest, 'w')

    for line in f_source:
        new_line = line.replace(pattern, replace)
        f_dest.wrote(new_line)

    f_source.close()
    f_dest.close()

    pattern = 'Jude'
    replace = 'Jack'
    source = 'Session-14/sed_tester.txt'
    dest = 'new_' + source
    sed(pattern, replace, source, dest)