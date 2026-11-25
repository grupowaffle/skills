// the news — preset Tailwind. Uso: presets: [require('./tailwind.preset.js')]
// Importe também tokens.css no CSS global (as cores semânticas vêm das variáveis, então dark mode funciona sozinho).
// O preset SUBSTITUI a paleta padrão do Tailwind: blue-500, gray-400 etc. deixam de existir de propósito.

module.exports = {
  theme: {
    colors: {
      transparent: 'transparent',
      current: 'currentColor',
      amarelo: '#ffcd00',
      laranja: '#ff8e42', // só em from-laranja to-amarelo
      preto: '#000000',
      branco: '#ffffff',
      surface: 'var(--surface)',
      'surface-alt': 'var(--surface-alt)',
      ink: 'var(--ink)',
      'ink-muted': 'var(--ink-muted)',
      line: 'var(--line)',
      'line-soft': 'var(--line-soft)',
      erro: 'var(--feedback-erro)',
      sucesso: 'var(--feedback-sucesso)',
      sub: { 1: 'var(--sub-1)', 2: 'var(--sub-2)' },
    },
    fontFamily: {
      display: ['"Helvetica Now Display"', '"Inter Tight"', 'Helvetica', 'Arial', 'sans-serif'],
      sans: ['"Helvetica Now Display"', '"Inter Tight"', 'Helvetica', 'Arial', 'sans-serif'],
      mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'], // só para código
    },
    fontWeight: { light: '300', normal: '400', bold: '700', extrabold: '800', black: '900' },
    borderRadius: { none: '0', pill: '16px', full: '9999px' },
    extend: {
      fontSize: {
        display: ['clamp(2.75rem, 6vw, 5.5rem)', { lineHeight: '1', letterSpacing: '-0.02em' }],
        h1: ['clamp(2.25rem, 4.5vw, 3.5rem)', { lineHeight: '1', letterSpacing: '-0.02em' }],
        h2: ['clamp(1.75rem, 3vw, 2.5rem)', { lineHeight: '1', letterSpacing: '-0.02em' }],
        h3: ['1.5rem', { lineHeight: '1.1', letterSpacing: '-0.02em' }],
        numero: ['clamp(2.5rem, 5vw, 4rem)', { lineHeight: '1', letterSpacing: '-0.02em' }],
        lead: ['1.375rem', { lineHeight: '1.35' }],
        body: ['1.125rem', { lineHeight: '1.45' }],
        small: ['0.9375rem', { lineHeight: '1.4' }],
        eyebrow: ['0.8125rem', { lineHeight: '1.2', letterSpacing: '0.04em' }],
      },
      letterSpacing: { titulo: '-0.02em' },
      spacing: { 'tn-1': '16px', 'tn-2': '32px', 'tn-3': '56px', 'tn-4': '108px', tarja: '6px', 'tarja-hero': '20px' },
      backgroundImage: {
        degrade: 'linear-gradient(90deg, #ff8e42 0%, #ffcd00 100%)',
        'degrade-v': 'linear-gradient(180deg, #ffcd00 0%, #ff8e42 100%)',
        'sub-degrade': 'linear-gradient(90deg, var(--sub-1), var(--sub-2))',
      },
      boxShadow: { none: 'none' },
    },
  },
};
