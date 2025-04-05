import { Component } from '@angular/core';
import { NavbarComponent } from '../../common/navbar/navbar.component';
import { ButtonComponent } from '../../common/button/button.component';
import { animate, state, style, transition, trigger, group, query } from '@angular/animations';

@Component({
  selector: 'app-my-decks',
  imports: [NavbarComponent, ButtonComponent],
  animations:[
    trigger('hideMenuContent', [
      state('shown', style({
        opacity: '1'
      })),
      state('hidden', style({
        opacity: '0'
      })),
      transition('shown <=> hidden', [
        animate('0.1s ease-out')
      ]),
    ]),
    trigger('hiddenShown', [
      state('shown', style({
        width: '300px'
      })),
      state('hidden', style({
        width: '20px'
      })),
      transition('shown <=> hidden', [
          animate('0.5s ease-out')
      ]),
    ])
  ],
  templateUrl: './my-decks.component.html',
  styleUrl: './my-decks.component.scss'
})
export class MyDecksComponent {
  public menuState: 'shown' | 'hidden' = 'shown'
  public menuContentState: 'shown' | 'hidden' = 'shown'
  changeState(){
    if(this.menuState == 'shown'){
      this.menuContentState = 'hidden'
      this.menuState = 'hidden';
    }
    else{
      this.menuContentState = 'shown'
      this.menuState = 'shown'
    }
  }
}
