import { Component } from '@angular/core';
import { NavbarComponent } from '../../common/navbar/navbar.component';
import { ButtonComponent } from '../../common/button/button.component';

@Component({
  selector: 'app-my-decks',
  imports: [NavbarComponent, ButtonComponent],
  templateUrl: './my-decks.component.html',
  styleUrl: './my-decks.component.scss'
})
export class MyDecksComponent {
  isCollapsed : Boolean = false;
  private collapseSideMenu(){
    
  }
  private showSideMenu(){
    //show side menu
  }
  changeSideMenuState(){
    if (this.isCollapsed){
      this.showSideMenu();
      this.isCollapsed = false;
    }
    else{
      this.collapseSideMenu();
      this.isCollapsed = true;
    }
  }
}
