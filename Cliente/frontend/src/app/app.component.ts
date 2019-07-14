import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';
import { Apicultor, Apiario, CaixaRacional, Perda } from './criacao';


@Component({
  selector: 'app-root',
  template: `<router-outlet></router-outlet>`
})
export class AppComponent implements OnInit {
    

  constructor(private api: ApiService){ }

  ngOnInit(){
  
  }

}
