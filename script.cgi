#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>NMAP On Browser"
echo "</title><meta http-equiv=”refresh” content=600></head><body>"
echo "<h1>Nmap</h1>"
echo "<h2>List Scan Result</h2>$(nmap -sL)\n<br>"
echo "<h2>Ping Scan Result</h2>$(nmap -sL)\n<br>"
echo "<h2>Scan result for top 100 ports</h2>$(nmap –top-ports 100)\n<br>"
echo "<h2>Nmap Version </h2>$(nmap -V)\n<br>"
echo "\n\n This report is generated at $(date) <p>
</p><button
onclick="window.print()">Save this page as PDF</button><br>"
echo "</body></html>"
