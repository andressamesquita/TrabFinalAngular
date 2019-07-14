import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { Apicultor, Apiario, CaixaRacional, Perda } from '../criacao';
import { listLazyRoutes } from '@angular/compiler/src/aot/lazy_routes';



@Component({
  selector: 'app-list',
  templateUrl: './list.component.html',
  styleUrls: ['./list.component.css'] 
  
})
export class ListComponent implements OnInit {

  apicultores: Apicultor[];
  error: any;

  constructor(private api: ApiService) { }

  ngOnInit() {
    this.api.getApicultor().subscribe(
      (apicultores: Apicultor[]) => this.apicultores = apicultores,
      (error: any) => this.error = error
    );
  }

  add(apicultorNome: string, qtdApiarios: number, tipo_criador: string) {
    this.api.createApicultor(apicultorNome, qtdApiarios, tipo_criador).subscribe(
      (apicultor: Apicultor) => this.apicultores.push(apicultor),
      (error: any) => this.error = error
    );
  }

  delete(id: number) {
    this.api.deleteApicultor(id).subscribe(
      (success: any) => this.apicultores.splice(
        this.apicultores.findIndex(apicultor => apicultor.id === id)
      ),
      (error: any) => this.error = error
    );
  }
  logout() {
    localStorage.removeItem('token');
    localStorage.removeItem('expires_at');
    location.reload();
  }
}
