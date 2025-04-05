import { Injectable } from '@angular/core';
import { BehaviorSubject } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthStateService {
  private isLoggedIn = new BehaviorSubject<boolean>(false);

  isLoggedIn$ = this.isLoggedIn.asObservable();
 
  constructor() { }

  setLoggedIn(isLoggedIn:boolean){
    this.isLoggedIn.next(isLoggedIn);
  }
  getLoggedIn():boolean{
    return this.isLoggedIn.value;
  }
}
