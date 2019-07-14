export interface Apicultor {
    id: number;
    nome: string;
    qtd_apiarios: number;
    tipo_criador: string;
}

export interface Apiario {
    id: number;
    apicultor: string;
    qtd_colmeias: number;
    localizador: string;
}

export interface CaixaRacional {
    id: number;
    apiario: string;
    identificador: string;
    localizador: string;
    especie: string;
}

export interface Perda {
    id: number;
    tipo_perda: string;
    qtd_colmeias_perdidas: number;
    especie_perdida: string;
    apiario: string;
}