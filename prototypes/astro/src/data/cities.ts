export interface City {
  slug: string;
  nome: string;
  eyebrow: string;
  progetti: number;
  desde: string;
  indirizzo: string;
  metro: string;
  orari: string;
  telefono: string;
}

export const cities: City[] = [
  {
    slug: 'milano',
    nome: 'Milano',
    eyebrow: 'MILANO E PROVINCIA',
    progetti: 14,
    desde: '2023',
    indirizzo: 'Via Andrea Solari 43, 20144 Milano (MI)',
    metro: 'M2 S. Agostino',
    orari: 'Lun–Ven 9:00–18:00',
    telefono: '+39 02 1234 5678',
  },
];
