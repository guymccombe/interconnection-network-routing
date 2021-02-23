def star5_routing(source, target):
    idx = len(source) - 1
    path = [source[:]]
    while source != target:
        target_index = source.index(target[idx])
        if idx == target_index:
            idx -= 1
        elif target_index == 0:
            source[idx], source[target_index] = source[target_index], source[idx]
            path.append(source[:])
        else:
            source[target_index], source[0] = source[0], source[target_index]
            path.append(source[:])
            source[idx], source[0] = source[0], source[idx]
            path.append(source[:])

    return path


def hypercube_routing(n, source, target):
    # [:] creates a copy to stop overwriting elements already in route
    route = [source[:]]
    while source != target:
        n = n - 1
        if source[n] != target[n]:
            source[n] = target[n]
            route.append(source[:])
    return route


def karyncube_routing(n, k, source, target):
    route = [source[:]]
    while source != target:
        n = n-1
        if source[n] != target[n]:
            direction = +1 if (source[n] - target[n]) % k >= k/2 else -1
            while source[n] != target[n]:
                source[n] = (source[n] + direction) % k
                route.append(source[:])
    return route


def cubeconncycle_routing(n, source, target):
    route = [source[:]]

    # generate list of indices where the nodes differ
    indices = [i for i, z in enumerate(
        zip(source[:-1], target[:-1])) if z[0] != z[1]]

    split_point = n - source[-1]
    for i in range(len(indices)):
        if indices[i] >= split_point:
            indices = indices[i:] + indices[:i]
            break

    for idx in indices:
        while n - source[-1] != idx:
            source[-1] = (source[-1] - 2) % n + 1
            route.append(source[:])
        source[idx] = target[idx]
        route.append(source[:])

    direction = +1 if (source[-1] - target[-1]) % n > n/2 else -1
    while source[-1] != target[-1]:
        source[-1] = (source[-1] + direction)
        if source[-1] == n+1:
            source[-1] = 1
        elif source[-1] == 0:
            source[-1] = n
        route.append(source[:])
    return route
