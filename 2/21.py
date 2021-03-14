def f21(x):
    if x[1] == 'asn.1':
        if x[4] == 1995:
            if x[3] == 'ec':
                return 0
            elif x[3] == 'opa':
                if x[2] == 'http':
                    return 1
                elif x[2] == 'xs':
                    return 2
                elif x[2] == 'vcl':
                    return 3
            elif x[3] == 'css':
                if x[2] == 'http':
                    return 4
                elif x[2] == 'xs':
                    return 5
                elif x[2] == 'vcl':
                    return 6
        elif x[4] == 2007:
            return 7
        elif x[4] == 1971:
            if x[3] == 'ec':
                return 8
            elif x[3] == 'opa':
                if x[0] == 1962:
                    return 9
                elif x[0] == 2019:
                    return 10
            elif x[3] == 'css':
                return 11
    elif x[1] == 'ston':
        return 12
    elif x[1] == 'chuck':
        return 13