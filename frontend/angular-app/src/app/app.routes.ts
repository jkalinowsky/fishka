import { Routes } from '@angular/router';
import { LandingPageComponent } from './views/landing-page/landing-page.component';
import { LoginComponent } from './views/login/login.component';
import { RegisterComponent } from './views/register/register.component';
import { MyDecksComponent } from './views/my-decks/my-decks.component';

export const routes: Routes = [
    {path:'', component:LandingPageComponent},
    {path:'login', component:LoginComponent},
    {path:'register', component:RegisterComponent},
    {path:'my-decks', component:MyDecksComponent}
];
