package main

import "testing"

func Test_fizzbuzz(t *testing.T) {
	type args struct {
		i int
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "Return number string",
			args: args{i: 1},
			want: "1",
		},
		{
			name: `Return "Fizz"`,
			args: args{i: 3},
			want: "Fizz",
		},
		{
			name: `Return "Buzz"`,
			args: args{i: 5},
			want: "Buzz",
		},
		{
			name: `Return "FizzBuzz"`,
			args: args{i: 15},
			want: "FizzBuzz",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := fizzbuzz(tt.args.i); got != tt.want {
				t.Errorf("fizzbuzz() = %v, want %v", got, tt.want)
			}
		})
	}
}
