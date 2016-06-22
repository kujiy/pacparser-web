// pacparser-web demo.pac
// Refer to http://findproxyforurl.com/pac-functions/

function FindProxyForURL(url, host)
{

    if ( dnsDomainIs( host, "example.com" ) ) {
        return "PROXY your-company-proxy:8080";
    }

    if ( shExpMatch( host, "localhost" ) ) {
        return "DIRECT";
    }

	if (isInNet(host, "127.0.0.1", "255.0.0.0") ) {
		return "DIRECT";
	}

    return "PROXY your-sub-proxy:3128";

}
