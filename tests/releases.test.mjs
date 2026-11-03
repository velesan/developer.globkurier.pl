import assert from 'node:assert/strict';
import { test } from 'node:test';

import { loadReleases, publishedReleases, releaseHtml } from '../docs/assets/releases.js';

const release = (overrides) => ({
  name: 'API 2026-11-03',
  tag_name: 'api-2026-11-03',
  html_url: 'https://github.com/velesan/developer.globkurier.pl/releases/tag/api-2026-11-03',
  published_at: '2026-11-03T10:00:00Z',
  body_html: '<ul><li>New field</li></ul>',
  draft: false,
  prerelease: false,
  ...overrides,
});

const container = () => ({
  dataset: { empty: 'No changes yet.', error: 'Could not load the changelog.' },
  innerHTML: 'Loading',
});

test('keeps published releases only, newest first', () => {
  const releases = [
    release({ tag_name: 'old', published_at: '2026-01-01T00:00:00Z' }),
    release({ tag_name: 'pre', prerelease: true }),
    release({ tag_name: 'draft', draft: true }),
    release({ tag_name: 'new', published_at: '2026-11-03T00:00:00Z' }),
  ];

  assert.deepEqual(publishedReleases(releases).map((r) => r.tag_name), ['new', 'old']);
});

test('renders name, localized date and GitHub-rendered body', () => {
  const html = releaseHtml(release(), 'pl');

  assert.match(html, /<h2 id="api-2026-11-03">API 2026-11-03<\/h2>/);
  assert.match(html, /3 listopada 2026/);
  assert.match(html, /<ul><li>New field<\/li><\/ul>/);
});

test('falls back to the tag and escapes the title', () => {
  assert.match(releaseHtml(release({ name: '' }), 'en'), />api-2026-11-03<\/h2>/);
  assert.match(releaseHtml(release({ name: '<b>x</b>' }), 'en'), />&lt;b&gt;x&lt;\/b&gt;<\/h2>/);
});

test('shows the empty text when there is no published release', async () => {
  const el = container();
  await loadReleases(el, 'en', async () => ({ ok: true, json: async () => [release({ prerelease: true })] }));

  assert.match(el.innerHTML, /No changes yet\./);
});

test('shows the error text when GitHub does not answer', async () => {
  const el = container();
  await loadReleases(el, 'en', async () => ({ ok: false, status: 403 }));

  assert.match(el.innerHTML, /Could not load the changelog\./);
});

test('asks GitHub for rendered HTML of all releases on one page', async () => {
  let request;
  await loadReleases(container(), 'en', async (url, options) => {
    request = { url, accept: options.headers.Accept };
    return { ok: true, json: async () => [] };
  });

  assert.equal(request.url, 'https://api.github.com/repos/velesan/developer.globkurier.pl/releases?per_page=100');
  assert.equal(request.accept, 'application/vnd.github.html+json');
});
