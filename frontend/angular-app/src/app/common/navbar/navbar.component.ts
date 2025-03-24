import { Component, OnInit } from '@angular/core';
import { AuthStateService } from '../../services/auth-state.service';
import { NgIf } from '@angular/common';
import { Router } from '@angular/router';

@Component({
  selector: 'app-navbar',
  imports: [NgIf],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss',
})
export class NavbarComponent implements OnInit {
  isLoggedIn = false;
  constructor(private authStateService: AuthStateService, private router:Router){}
  ngOnInit(): void {
    this.authStateService.isLoggedIn$.subscribe((isLoggedIn: boolean)=>{
      this.isLoggedIn = isLoggedIn;
    })
  }
  goHome(){
    this.router.navigate(['/']);
  }
  goToLogin(){
    this.router.navigate(['/login']);
  }
  goToRegister(){
    this.router.navigate(['/register']);
  }
}
