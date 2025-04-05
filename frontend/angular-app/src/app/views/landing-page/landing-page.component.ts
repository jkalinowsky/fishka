import { Component } from '@angular/core';
import { AuthStateService } from '../../services/auth-state.service';
import { NgIf } from '@angular/common';
import { NavbarComponent } from "../../common/navbar/navbar.component";

@Component({
  selector: 'app-landing-page',
  imports: [NavbarComponent],
  templateUrl: './landing-page.component.html',
  styleUrl: './landing-page.component.scss'
})
export class LandingPageComponent {
  isLoggedIn = false;
  constructor(private authStateService: AuthStateService){}
  ngOnInit(): void {
    this.authStateService.isLoggedIn$.subscribe(isLoggedIn=>{
      this.isLoggedIn = isLoggedIn;
    })
  }
}
