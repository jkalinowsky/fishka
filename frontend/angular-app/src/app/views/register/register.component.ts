import { Component } from '@angular/core';
import { AuthStateService } from '../../services/auth-state.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';
import { ButtonComponent } from "../../common/button/button.component";
import { NavbarComponent } from '../../common/navbar/navbar.component';

@Component({
  selector: 'app-register',
  imports: [FormsModule, ButtonComponent, NavbarComponent],
  templateUrl: './register.component.html',
  styleUrl: './register.component.scss'
})
export class RegisterComponent {

  login_prop: String = "";
  password_prop: String = "";

  constructor(private authStateService: AuthStateService, private router: Router){}
  goBackHome(){
    this.router.navigate(['/']);
  }
  register() : void{
    this.authStateService.setLoggedIn(true);
  }
}
