from datetime import datetime

urls = [
    {"loc": "http://localhost:1313/blog/", "lastmod": "2024-07-01T12:08:39-05:00", "changefreq": "weekly", "priority": "0.8"},
    {"loc": "http://localhost:1313/blog/test_tufte/", "lastmod": "2024-07-01T12:08:39-05:00", "changefreq": "monthly", "priority": "0.5"},
    {"loc": "http://localhost:1313/thematrix/", "lastmod": "2024-06-05T16:17:44-05:00", "changefreq": "monthly", "priority": "0.7"},
    {"loc": "http://localhost:1313/blog/programming/", "lastmod": "2024-05-30T13:44:46-05:00", "changefreq": "weekly", "priority": "0.6"},
    {"loc": "http://localhost:1313/current/", "lastmod": "2024-05-22T11:05:27-05:00", "changefreq": "weekly", "priority": "0.9"},
    {"loc": "http://localhost:1313/blog/philosophy/", "lastmod": "2024-05-22T10:47:04-05:00", "changefreq": "monthly", "priority": "0.5"},
    {"loc": "http://localhost:1313/", "lastmod": "2024-05-21T00:00:00+00:00", "changefreq": "daily", "priority": "1.0"},
    {"loc": "http://localhost:1313/categories/", "changefreq": "monthly", "priority": "0.3"},
    {"loc": "http://localhost:1313/tags/", "changefreq": "monthly", "priority": "0.3"},
]

sitemap_template = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls}
</urlset>
"""

url_template = """  <url>
    <loc>{loc}</loc>
    {lastmod}
    <changefreq>{changefreq}</changefreq>
    <priority>{priority}</priority>
  </url>"""

url_entries = []

for url in urls:
    lastmod_tag = f"<lastmod>{url['lastmod']}</lastmod>" if 'lastmod' in url else ""
    url_entries.append(url_template.format(
        loc=url["loc"],
        lastmod=lastmod_tag,
        changefreq=url["changefreq"],
        priority=url["priority"]
    ))

sitemap_content = sitemap_template.format(urls="\n".join(url_entries))

print(sitemap_content)

