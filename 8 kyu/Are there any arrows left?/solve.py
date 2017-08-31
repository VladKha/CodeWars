def any_arrows(arrows):
    return any(a.get('damaged', False) is False for a in arrows)
