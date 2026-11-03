// The API changelog is the list of GitHub Releases, loaded in the browser so a release needs no portal rebuild.
const RELEASES_API = 'https://api.github.com/repos/velesan/developer.globkurier.pl/releases?per_page=100';

export function publishedReleases(releases) {
  return releases
    .filter((release) => !release.draft && !release.prerelease)
    .sort((a, b) => b.published_at.localeCompare(a.published_at));
}

export function releaseHtml(release, lang) {
  const date = new Intl.DateTimeFormat(lang, { dateStyle: 'long', timeZone: 'UTC' }).format(new Date(release.published_at));
  const id = release.tag_name.toLowerCase().replace(/[^a-z0-9.-]+/g, '-');

  // body_html is rendered and sanitized by GitHub (Accept: application/vnd.github.html+json).
  return `<section class="api-release">
<h2 id="${id}">${escapeHtml(release.name || release.tag_name)}</h2>
<p class="api-release__date"><a href="${escapeHtml(release.html_url)}">${date}</a></p>
${release.body_html || ''}
</section>`;
}

export async function loadReleases(container, lang, fetchFn) {
  try {
    const response = await fetchFn(RELEASES_API, { headers: { Accept: 'application/vnd.github.html+json' } });
    if (!response.ok) {
      throw new Error(`GitHub API ${response.status}`);
    }
    const releases = publishedReleases(await response.json());
    container.innerHTML = releases.length
      ? releases.map((release) => releaseHtml(release, lang)).join('\n')
      : `<p>${escapeHtml(container.dataset.empty)}</p>`;
  } catch {
    container.innerHTML = `<p>${escapeHtml(container.dataset.error)}</p>`;
  }
}

const HTML_ENTITIES = { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' };

function escapeHtml(text) {
  return String(text).replace(/[&<>"']/g, (char) => HTML_ENTITIES[char]);
}

const container = typeof document !== 'undefined' && document.getElementById('api-releases');
if (container) {
  loadReleases(container, document.documentElement.lang, fetch);
}
