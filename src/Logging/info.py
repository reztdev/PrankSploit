#!/usr/bin/python

exploit = {
    "crack" : {
        "name_exploit" : "PyCracker",
        "location" : "exploit/crack/hash",
        "support_hash" : [
            "MD5",
            "SHA1",
            "SHA128",
            "SHA256",
            "SHA384",
            "SHA512"
        ],
        "author" : "Mochammad Rizki",
        "codename" : "ReztDev",
        "version" : "1.5",
        "description" : "Cracking password using brute force file wordlist path"
    },

    "admin_finder" : {
        "name_exploit" : "Admin Finder",
        "location" : "exploit/scanner/admin_finder",
        "author" : "Mochammad Rizki",
        "codename" : "ReztDev",
        "version" : "1.7",
        "description" : "Scanner Admin Login on Website"
    },

    "udp_flood" : {
        "name_exploit" : "UDP Flooder",
        "location" : "exploit/attack/udp_flood",
        "author" : "Mochammad Rizki",
        "codename" : "ReztDev",
        "version" : "1.0",
        "description" : "DDOS Attack with send data UDP Protocol"
    },

    "ftp_brute" : {
        "name_exploit" : "FTP Brute Force",
        "location" : "exploit/brute/ftp_brute",
        "author" : "Mochammad Rizki",
        "codename" : "ReztDev",
        "version" : "1.4.",
        "description" : "Brute Forcing FTP (File Transfer Protocol) on port (default 21) using wordlist"
    },

}

Payloads = {
    "BSOD" : {
        "name_exploit" : "Blue Screen Of Death Payloads",
        "location" : "modules/payload/bluesc",
        "author" : "Mochammad Rizki",
        "codename" : "ReztDev",
        "version" : "1.0.0",
        "description" : "Payload Blue Screen Of Death for Windows System"
    },

    "caplock" : {
        "name_exploit" : "Caplock Error",
        "location" : "modules/payload/caplock",
        "author" : "Mochammad Rizki",
        "codename" : "ReztDev",
        "description" : "Payload Caplock Error on keyboard target"
    },

    "CDROM" : {
        ""
    }
}