<a name="App Functions SDK ChangeLog"></a>
## App Functions SDK (in Python)
[Github repository](https://github.com/edgexfoundry/app-functions-sdk-python)

### Change Logs for EdgeX Dependencies
- [go-mod-bootstrap](https://github.com/edgexfoundry/go-mod-bootstrap/blob/main/CHANGELOG.md)
- [go-mod-core-contracts](https://github.com/edgexfoundry/go-mod-core-contracts/blob/main/CHANGELOG.md)
- [go-mod-messaging](https://github.com/edgexfoundry/go-mod-messaging/blob/main/CHANGELOG.md)
- [go-mod-registry](https://github.com/edgexfoundry/go-mod-registry/blob/main/CHANGELOG.md) 
- [go-mod-configuration](https://github.com/edgexfoundry/go-mod-configuration/blob/main/CHANGELOG.md) (indirect dependency)
- [go-mod-secrets](https://github.com/edgexfoundry/go-mod-secrets/blob/main/CHANGELOG.md) (indirect dependency)

## [4.0.0] Odessa - 2025-03-12 (Only compatible with the 4.x releases)

### ✨  Features

- Use normal JSON object in message envelope payload instead of base64 ([07da012…](https://github.com/edgexfoundry/app-functions-sdk-python/commit/07da012751ab8e07904a79dfbc144b316d1d7574))
```text

BREAKING CHANGE: Change MessageEnvelope payload from a byte array to a generic type

```

