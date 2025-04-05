import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-button',
  imports: [],
  templateUrl: './button.component.html',
  styleUrl: './button.component.scss'
})
export class ButtonComponent {
  @Input() value: string = 'Kliknij mnie';
  @Input() action!: () => void;
  onClick(): void{
    if(this.action)
    {
      this.action()
    }
  }
}
