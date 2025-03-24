import { Component } from '@angular/core';
import { AuthStateService } from '../../services/auth-state.service';
import { Router } from '@angular/router';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-register',
  imports: [FormsModule],
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
  login() : void{
    this.authStateService.setLoggedIn(true);
  }
}
