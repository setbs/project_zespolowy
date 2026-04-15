from fastapi.responses import HTMLResponse


def frontend_page() -> HTMLResponse:
    html = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>MusicRate</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #0b1020;
      --panel: rgba(17, 24, 39, 0.82);
      --text: #e5eefb;
      --muted: #8aa0bf;
      --line: rgba(148, 163, 184, 0.18);
      --accent: #34d399;
      --accent-2: #60a5fa;
      --danger: #fb7185;
      --shadow: 0 24px 80px rgba(0, 0, 0, 0.35);
      --radius: 22px;
    }

    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      color: var(--text);
      background:
        radial-gradient(circle at top left, rgba(96, 165, 250, 0.16), transparent 28%),
        radial-gradient(circle at top right, rgba(52, 211, 153, 0.15), transparent 26%),
        linear-gradient(180deg, #050816 0%, var(--bg) 100%);
      min-height: 100vh;
    }

    .page { width: min(1180px, calc(100% - 32px)); margin: 0 auto; padding: 28px 0 40px; }
    .hero { display: grid; grid-template-columns: 1.5fr 1fr; gap: 18px; margin-bottom: 18px; }
    .panel { background: var(--panel); border: 1px solid var(--line); border-radius: var(--radius); box-shadow: var(--shadow); backdrop-filter: blur(18px); }
    .hero-main, .hero-side, .section { padding: 20px; }
    .hero-main { position: relative; overflow: hidden; }
    .eyebrow { display: inline-flex; gap: 8px; align-items: center; padding: 8px 12px; border-radius: 999px; background: rgba(52, 211, 153, 0.12); color: #b8ffe1; font-size: 12px; letter-spacing: 0.08em; text-transform: uppercase; }
    h1 { margin: 18px 0 12px; font-size: clamp(36px, 5vw, 60px); line-height: 0.95; letter-spacing: -0.05em; }
    .lead { max-width: 58ch; color: var(--muted); line-height: 1.65; margin: 0; }
    .hero-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; margin-top: 22px; }
    .stat { padding: 14px 16px; border-radius: 18px; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.05); }
    .stat span { display: block; color: var(--muted); font-size: 12px; margin-bottom: 6px; }
    .stat strong { font-size: 18px; }
    .hero-side { display: grid; gap: 14px; }
    .hero-auth { display: grid; grid-template-columns: 1fr 1fr; gap: 14px; }
    .card { padding: 18px; border-radius: 18px; background: rgba(15, 23, 42, 0.92); border: 1px solid var(--line); }
    .card h2, .card h3, .section h2 { margin: 0 0 14px; font-size: 18px; }
    .grid { display: grid; grid-template-columns: 1fr 1fr; gap: 18px; margin-top: 18px; }
    .grid.single { grid-template-columns: 1fr; }
    .section-head { margin-bottom: 16px; }
    .section-head p { margin: 4px 0 0; color: var(--muted); font-size: 14px; }
    .toolbar { display: flex; gap: 10px; flex-wrap: wrap; }
    input, textarea, select, button { font: inherit; }
    input, textarea, select { width: 100%; padding: 12px 14px; border-radius: 14px; border: 1px solid rgba(148, 163, 184, 0.2); background: rgba(2, 6, 23, 0.6); color: var(--text); outline: none; }
    textarea { min-height: 110px; resize: vertical; }
    button { border: 0; cursor: pointer; padding: 12px 16px; border-radius: 14px; background: linear-gradient(135deg, var(--accent), #22c55e); color: #06121a; font-weight: 700; transition: transform 0.15s ease, opacity 0.15s ease; }
    button.secondary { background: rgba(96, 165, 250, 0.16); color: var(--text); border: 1px solid rgba(96, 165, 250, 0.25); }
    button.ghost { background: rgba(255, 255, 255, 0.06); color: var(--text); border: 1px solid rgba(255, 255, 255, 0.08); }
    button:hover { transform: translateY(-1px); }
    button:disabled { opacity: 0.55; cursor: not-allowed; transform: none; }
    .form { display: grid; gap: 10px; }
    .form-row { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 10px; }
    .message { min-height: 20px; color: var(--muted); font-size: 14px; }
    .message.error { color: #fda4af; }
    .message.ok { color: #86efac; }
    .list { display: grid; gap: 12px; }
    .item { display: grid; grid-template-columns: 64px 1fr auto; gap: 14px; align-items: center; padding: 14px; border-radius: 18px; background: rgba(255, 255, 255, 0.04); border: 1px solid rgba(255, 255, 255, 0.05); }
    .cover { width: 64px; height: 64px; border-radius: 14px; background: linear-gradient(135deg, rgba(96, 165, 250, 0.45), rgba(52, 211, 153, 0.35)); display: grid; place-items: center; color: #fff; font-weight: 700; overflow: hidden; }
    .cover img { width: 100%; height: 100%; object-fit: cover; display: block; }
    .meta h4 { margin: 0 0 4px; font-size: 16px; }
    .meta p { margin: 0; color: var(--muted); font-size: 13px; }
    .badge { display: inline-flex; align-items: center; gap: 6px; padding: 8px 10px; border-radius: 999px; background: rgba(52, 211, 153, 0.12); color: #bbf7d0; font-size: 13px; white-space: nowrap; }
    .small { color: var(--muted); font-size: 12px; }
    .footer-note { margin-top: 16px; color: var(--muted); font-size: 13px; line-height: 1.6; }
    @media (max-width: 900px) { .hero, .grid, .hero-auth { grid-template-columns: 1fr; } .hero-stats { grid-template-columns: 1fr; } .item { grid-template-columns: 52px 1fr; } .item .badge { grid-column: 2; justify-self: start; } .form-row { grid-template-columns: 1fr; } }
  </style>
</head>
<body>
  <div class="page">
    <section class="hero">
      <div class="panel hero-main">
        <div class="eyebrow">MusicRate MVP · FastAPI + PostgreSQL + Last.fm</div>
        <h1>Rate albums, keep reviews, and browse music in one place.</h1>
        <p class="lead">This is a minimal but working demo frontend for the project. It connects to the backend API, supports user registration/login, loads albums, creates ratings, and can query Last.fm search results.</p>
        <div class="hero-stats">
          <div class="stat"><span>Backend</span><strong>FastAPI</strong></div>
          <div class="stat"><span>Database</span><strong>SQLite / PostgreSQL</strong></div>
          <div class="stat"><span>External API</span><strong>Last.fm</strong></div>
        </div>
      </div>
      <div class="panel hero-side">
        <div class="hero-auth">
          <div class="card">
            <h3>Register</h3>
            <div class="form">
              <input id="regEmail" type="email" placeholder="Email" />
              <input id="regUsername" type="text" placeholder="Username" />
              <input id="regPassword" type="password" placeholder="Password (min 8 chars)" />
              <button id="registerBtn" type="button">Create account</button>
            </div>
            <div id="registerMessage" class="message"></div>
          </div>

          <div class="card">
            <h3>Login</h3>
            <div class="form">
              <input id="loginEmail" type="email" placeholder="Email" />
              <input id="loginPassword" type="password" placeholder="Password" />
              <button id="loginBtn" type="button">Sign in</button>
            </div>
            <div id="loginMessage" class="message"></div>
          </div>
        </div>

        <div class="card">
          <h3>Session</h3>
          <div class="small">Token is stored locally after login for demo purposes.</div>
          <div id="sessionStatus" class="message">Not signed in.</div>
          <div class="toolbar">
            <button class="secondary" id="refreshBtn" type="button">Reload data</button>
            <button class="ghost" id="clearTokenBtn" type="button">Clear token</button>
          </div>
        </div>
        <div class="card">
          <h3>Quick API links</h3>
          <div class="toolbar">
            <button class="ghost" type="button" onclick="window.open('/docs', '_blank')">Open Swagger</button>
            <button class="ghost" type="button" onclick="window.open('/redoc', '_blank')">Open ReDoc</button>
          </div>
        </div>
      </div>
    </section>

    <section class="grid single">
      <div class="panel section">
        <div class="section-head">
          <h2>Last.fm search</h2>
          <p>Search albums and then copy the result into the local catalog.</p>
        </div>
        <div class="toolbar" style="margin-bottom:12px">
          <input id="lastfmQuery" type="text" placeholder="Search album title" style="flex:1" />
          <button id="searchLastfmBtn" type="button">Search</button>
        </div>
        <div id="lastfmMessage" class="message"></div>
        <div id="lastfmResults" class="list"></div>
      </div>
    </section>

    <section class="grid">
      <div class="panel section">
        <div class="section-head">
          <h2>Albums</h2>
          <p>Stored in the backend database.</p>
        </div>
        <form id="albumForm" class="form">
          <div class="form-row">
            <input id="albumTitle" type="text" placeholder="Title" />
            <input id="albumArtist" type="text" placeholder="Artist" />
          </div>
          <div class="form-row">
            <input id="albumGenre" type="text" placeholder="Genre" />
            <input id="albumYear" type="number" placeholder="Year" />
          </div>
          <input id="albumCover" type="url" placeholder="Cover URL" />
          <button type="submit">Add album</button>
        </form>
        <div id="albumMessage" class="message"></div>
        <div id="albumsList" class="list" style="margin-top:14px"></div>
      </div>

      <div class="panel section">
        <div class="section-head">
          <h2>Ratings</h2>
          <p>Create a review for an album.</p>
        </div>
        <form id="ratingForm" class="form">
          <select id="ratingAlbum"></select>
          <div class="form-row">
            <input id="ratingScore" type="number" min="1" max="10" placeholder="Score 1-10" />
            <input id="ratingReviewShort" type="text" placeholder="Short note" />
          </div>
          <textarea id="ratingReview" placeholder="Review"></textarea>
          <button type="submit">Save rating</button>
        </form>
        <div id="ratingMessage" class="message"></div>
        <div id="ratingsList" class="list" style="margin-top:14px"></div>
      </div>
    </section>

    <div class="footer-note">
      This frontend is intentionally minimal. It is meant to prove that the project already has a working browser UI, API integration, and data flow for the demo stage.
    </div>
  </div>

  <script>
    const state = {
      token: localStorage.getItem('musicrate_token') || '',
      albums: [],
      ratings: [],
    };

    const $ = (id) => document.getElementById(id);

    function setMessage(id, text, kind = '') {
      const node = $(id);
      node.textContent = text;
      node.className = kind ? `message ${kind}` : 'message';
    }

    async function api(path, options = {}) {
      const response = await fetch(path, {
        headers: { 'Content-Type': 'application/json', ...(options.headers || {}) },
        ...options,
      });
      const contentType = response.headers.get('content-type') || '';
      const data = contentType.includes('application/json') ? await response.json() : await response.text();
      if (!response.ok) {
        const detail = typeof data === 'string' ? data : (data.detail || JSON.stringify(data));
        throw new Error(detail || `Request failed with ${response.status}`);
      }
      return data;
    }

    function renderSession() {
      const message = state.token ? 'Signed in. Token stored in localStorage.' : 'Not signed in.';
      setMessage('sessionStatus', message, state.token ? 'ok' : '');
    }

    function coverMarkup(album) {
      if (album.cover_url) {
        return `<div class="cover"><img src="${album.cover_url}" alt="${album.title}"></div>`;
      }
      const initials = (album.title || '?').slice(0, 2).toUpperCase();
      return `<div class="cover">${initials}</div>`;
    }

    function renderAlbumCards() {
      const list = $('albumsList');
      const select = $('ratingAlbum');
      select.innerHTML = state.albums.length
        ? state.albums.map((album) => `<option value="${album.id}">${album.title} — ${album.artist}</option>`).join('')
        : '<option value="">No albums</option>';

      list.innerHTML = state.albums.length
        ? state.albums.map((album) => `
          <article class="item">
            ${coverMarkup(album)}
            <div class="meta">
              <h4>${album.title}</h4>
              <p>${album.artist}${album.year ? ` · ${album.year}` : ''}${album.genre ? ` · ${album.genre}` : ''}</p>
              <p>Average rating: ${Number(album.avg_rating || 0).toFixed(1)}</p>
            </div>
            <span class="badge">ID ${album.id}</span>
          </article>
        `).join('')
        : '<div class="small">No albums yet. Add one manually or use Last.fm search.</div>';
    }

    function renderRatings() {
      const list = $('ratingsList');
      list.innerHTML = state.ratings.length
        ? state.ratings.map((rating) => `
          <article class="item">
            <div class="cover">${rating.score}</div>
            <div class="meta">
              <h4>Album #${rating.album_id}</h4>
              <p>${rating.review || 'No review'}</p>
              <p>User #${rating.user_id}</p>
            </div>
            <span class="badge">${rating.score}/10</span>
          </article>
        `).join('')
        : '<div class="small">No ratings yet.</div>';
    }

    async function loadAlbums() {
      const albums = await api('/api/v1/albums');
      state.albums = albums;
      renderAlbumCards();
    }

    async function loadRatings() {
      const ratings = await api('/api/v1/ratings');
      state.ratings = ratings;
      renderRatings();
    }

    async function loadAll() {
      await Promise.all([loadAlbums(), loadRatings()]);
      renderSession();
    }

    $('registerBtn').addEventListener('click', async () => {
      try {
        const payload = {
          email: $('regEmail').value.trim(),
          username: $('regUsername').value.trim(),
          password: $('regPassword').value,
        };
        await api('/api/v1/auth/register', {
          method: 'POST',
          body: JSON.stringify(payload),
        });
        setMessage('registerMessage', 'Registration successful. Now log in.', 'ok');
      } catch (error) {
        setMessage('registerMessage', error.message, 'error');
      }
    });

    $('loginBtn').addEventListener('click', async () => {
      try {
        const payload = {
          email: $('loginEmail').value.trim(),
          password: $('loginPassword').value,
        };
        const data = await api('/api/v1/auth/login', {
          method: 'POST',
          body: JSON.stringify(payload),
        });
        state.token = data.access_token;
        localStorage.setItem('musicrate_token', state.token);
        renderSession();
        setMessage('loginMessage', 'Login successful. Token saved locally.', 'ok');
      } catch (error) {
        setMessage('loginMessage', error.message, 'error');
      }
    });

    $('clearTokenBtn').addEventListener('click', () => {
      state.token = '';
      localStorage.removeItem('musicrate_token');
      renderSession();
    });

    $('refreshBtn').addEventListener('click', async () => {
      try {
        setMessage('albumMessage', 'Refreshing...', '');
        await loadAll();
        setMessage('albumMessage', 'Data refreshed.', 'ok');
      } catch (error) {
        setMessage('albumMessage', error.message, 'error');
      }
    });

    $('albumForm').addEventListener('submit', async (event) => {
      event.preventDefault();
      try {
        const payload = {
          title: $('albumTitle').value.trim(),
          artist: $('albumArtist').value.trim(),
          genre: $('albumGenre').value.trim() || null,
          year: $('albumYear').value ? Number($('albumYear').value) : null,
          cover_url: $('albumCover').value.trim() || null,
        };
        await api('/api/v1/albums', {
          method: 'POST',
          body: JSON.stringify(payload),
        });
        setMessage('albumMessage', 'Album added.', 'ok');
        event.target.reset();
        await loadAlbums();
      } catch (error) {
        setMessage('albumMessage', error.message, 'error');
      }
    });

    $('ratingForm').addEventListener('submit', async (event) => {
      event.preventDefault();
      try {
        const payload = {
          album_id: Number($('ratingAlbum').value),
          score: Number($('ratingScore').value),
          review: $('ratingReview').value.trim() || $('ratingReviewShort').value.trim() || null,
        };
        await api('/api/v1/ratings', {
          method: 'POST',
          body: JSON.stringify(payload),
        });
        setMessage('ratingMessage', 'Rating saved.', 'ok');
        event.target.reset();
        await loadRatings();
      } catch (error) {
        setMessage('ratingMessage', error.message, 'error');
      }
    });

    $('searchLastfmBtn').addEventListener('click', async () => {
      try {
        const query = $('lastfmQuery').value.trim();
        if (!query) {
          setMessage('lastfmMessage', 'Enter a search query.', 'error');
          return;
        }
        setMessage('lastfmMessage', 'Searching Last.fm...', '');
        const data = await api(`/api/v1/lastfm/search/album?q=${encodeURIComponent(query)}`);
        const matches = (data?.results?.albummatches?.album || []).slice(0, 6);
        $('lastfmResults').innerHTML = matches.length
          ? matches.map((album) => {
              const title = album.name || 'Unknown title';
              const artist = album.artist || 'Unknown artist';
              const image = Array.isArray(album.image) ? album.image[album.image.length - 1]?.['#text'] : '';
              const payload = encodeURIComponent(JSON.stringify({ title, artist, cover_url: image || '' }));
              return `
                <article class="item">
                  <div class="cover">${image ? `<img src="${image}" alt="${title}">` : title.slice(0, 2).toUpperCase()}</div>
                  <div class="meta">
                    <h4>${title}</h4>
                    <p>${artist}</p>
                  </div>
                  <button class="ghost" type="button" data-album="${payload}">Save</button>
                </article>
              `;
            }).join('')
          : '<div class="small">No Last.fm results found.</div>';
        setMessage('lastfmMessage', `Found ${matches.length} album(s).`, 'ok');
      } catch (error) {
        setMessage('lastfmMessage', error.message, 'error');
      }
    });

    $('lastfmResults').addEventListener('click', async (event) => {
      const button = event.target.closest('button[data-album]');
      if (!button) return;
      try {
        const album = JSON.parse(decodeURIComponent(button.dataset.album));
        await api('/api/v1/albums', {
          method: 'POST',
          body: JSON.stringify({
            title: album.title,
            artist: album.artist,
            genre: null,
            year: null,
            cover_url: album.cover_url || null,
          }),
        });
        await loadAlbums();
        setMessage('albumMessage', 'Album copied from Last.fm search.', 'ok');
      } catch (error) {
        setMessage('albumMessage', error.message, 'error');
      }
    });

    loadAll().catch((error) => {
      setMessage('albumMessage', error.message, 'error');
      setMessage('ratingMessage', error.message, 'error');
    });
  </script>
</body>
</html>"""
    return HTMLResponse(content=html)