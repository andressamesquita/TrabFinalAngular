import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';


@Injectable({
  providedIn: 'root'
})

export class ApiService {

  private apiRoot = 'http://localhost:8000/'
  
  constructor(private http:HttpClient) { }


  getApicultor(){
    return this.http.get(this.apiRoot.concat('apicultores/'));
  }

  getApiario(){
    return this.http.get(this.apiRoot.concat('apiarios/'));
  }

  getCaixaRacional(){
    return this.http.get(this.apiRoot.concat('caixas_racionais/'));
  }

  getPerda(){
    return this.http.get(this.apiRoot.concat('perdas/'));
  }

  createApicultor(nome: string, qtd_apiarios: number, tipo_criador: string) {
    return this.http.post(
      this.apiRoot.concat('apicultores/'),
      { nome, qtd_apiarios, tipo_criador }
    );
  }

  deleteApicultor(id: number) {
    return this.http.delete(this.apiRoot.concat(`apicultores/${id}/`));
  }

}
