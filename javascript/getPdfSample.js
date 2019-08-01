// ページからリンク先のpdfをダウンロードする
searchAttribute = "ng-click";
arefs = document.getElementsByTagName("a");

for (var aref of arefs) {
	if (aref.getAttribute(searchAttribute) != null) {
	// console.log(aref)
	aref.click()
	}
}

