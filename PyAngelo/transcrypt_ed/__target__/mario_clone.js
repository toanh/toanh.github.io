// Transcrypt'ed from Python, 2020-04-12 10:51:18
import {AssertionError, AttributeError, BaseException, DeprecationWarning, Exception, IndexError, IterableError, KeyError, NotImplementedError, RuntimeWarning, StopIteration, UserWarning, ValueError, Warning, __JsIterator__, __PyIterator__, __Terminal__, __add__, __and__, __call__, __class__, __envir__, __eq__, __floordiv__, __ge__, __get__, __getcm__, __getitem__, __getslice__, __getsm__, __gt__, __i__, __iadd__, __iand__, __idiv__, __ijsmod__, __ilshift__, __imatmul__, __imod__, __imul__, __in__, __init__, __ior__, __ipow__, __irshift__, __isub__, __ixor__, __jsUsePyNext__, __jsmod__, __k__, __kwargtrans__, __le__, __lshift__, __lt__, __matmul__, __mergefields__, __mergekwargtrans__, __mod__, __mul__, __ne__, __neg__, __nest__, __or__, __pow__, __pragma__, __proxy__, __pyUseJsNext__, __rshift__, __setitem__, __setproperty__, __setslice__, __sort__, __specialattrib__, __sub__, __super__, __t__, __terminal__, __truediv__, __withblock__, __xor__, abs, all, any, assert, bool, bytearray, bytes, callable, chr, copy, deepcopy, delattr, dict, dir, divmod, enumerate, filter, float, getattr, hasattr, input, int, isinstance, issubclass, len, list, map, max, min, object, ord, pow, print, property, py_TypeError, py_iter, py_metatype, py_next, py_reversed, py_typeof, range, repr, round, set, setattr, sorted, str, sum, tuple, zip} from './org.transcrypt.__runtime__.js';
import {CMD_CLEAR, CMD_DRAWCIRCLE, CMD_DRAWIMAGE, CMD_DRAWLINE, CMD_DRAWPIXEL, CMD_DRAWRECT, CMD_DRAWTEXT, CMD_HALT, CMD_INPUT, CMD_LOADSOUND, CMD_PAUSESOUND, CMD_PLAYSOUND, CMD_PRINT, CMD_REVEAL, Circle, Colour, KEY_A, KEY_BEGIN, KEY_CTRL, KEY_D, KEY_DOWN, KEY_END, KEY_ENTER, KEY_ESC, KEY_HOME, KEY_J, KEY_LEFT, KEY_PAGEDOWN, KEY_PAGEUP, KEY_Q, KEY_RIGHT, KEY_S, KEY_UP, KEY_V_DOWN, KEY_V_FIRE, KEY_V_LEFT, KEY_V_RIGHT, KEY_V_UP, KEY_W, Point, PyAngelo, PyAngeloImage, Rectangle, Sprite, Text, TextSprite, graphics} from './PyAngelo.js';
var __name__ = '__main__';
export var music = graphics.loadSound ('sounds/JeroenTel001.mp3');
graphics.playSound (music);
export var level_width = 950;
export var player = Sprite ('https://i.imgur.com/wDa6mLI.png', __kwargtrans__ ({x: 0, y: 20}));
player.y_dir = 0;
player.x_dir = 0;
player.score = 0;
player.lives = 1;
player.can_jump = false;
export var floors = [];
floors.append (Sprite (Rectangle (0, 0, 730, 20), __kwargtrans__ ({r: 0.5, g: 1, b: 0.5})));
floors.append (Sprite (Rectangle (800, 0, 300, 20), __kwargtrans__ ({r: 0.5, g: 1, b: 0.5})));
floors.append (Sprite (Rectangle (300, 100, 100, 20), __kwargtrans__ ({r: 0.5, g: 1, b: 0.5})));
floors.append (Sprite (Rectangle (200, 200, 100, 20), __kwargtrans__ ({r: 0.5, g: 1, b: 0.5})));
export var walls = [];
walls.append (Sprite ('https://i.imgur.com/VqmtsEo.png', __kwargtrans__ ({x: 450, y: 20, r: 0, g: 0, b: 1})));
walls.append (Sprite ('https://i.imgur.com/VqmtsEo.png', __kwargtrans__ ({x: 100, y: 20, r: 0, g: 0, b: 1})));
walls.append (Sprite (Rectangle (100, 120, 20, 20), __kwargtrans__ ({r: 0.2, g: 0.2, b: 1})));
walls.append (Sprite (Rectangle (800, 20, 150, 20), __kwargtrans__ ({r: 0.2, g: 0.2, b: 1})));
walls.append (Sprite (Rectangle (820, 40, 130, 20), __kwargtrans__ ({r: 0.3, g: 0.3, b: 1})));
walls.append (Sprite (Rectangle (840, 60, 110, 20), __kwargtrans__ ({r: 0.4, g: 0.4, b: 1})));
walls.append (Sprite (Rectangle (860, 80, 90, 20), __kwargtrans__ ({r: 0.5, g: 0.5, b: 1})));
walls.append (Sprite (Rectangle (880, 100, 70, 20), __kwargtrans__ ({r: 0.6, g: 0.6, b: 1})));
walls.append (Sprite (Rectangle (900, 120, 50, 20), __kwargtrans__ ({r: 0.7, g: 0.7, b: 1})));
export var hidden_wall = Sprite (Rectangle (690, 80, 20, 20), __kwargtrans__ ({r: 1, g: 1, b: 0}));
hidden_wall.py_metatype = 1;
walls.append (hidden_wall);
walls.append (Sprite (Rectangle (-(1), 0, 1, 1000), __kwargtrans__ ({r: 0.7, g: 0.7, b: 1})));
walls.append (Sprite (Rectangle (951, 0, 1, 1000), __kwargtrans__ ({r: 0.7, g: 0.7, b: 1})));
export var collects = [];
collects.append (Sprite ('https://i.imgur.com/jgIxuG7.png', 100, 200));
collects.append (Sprite ('https://i.imgur.com/jgIxuG7.png', 200, 260));
collects.append (Sprite ('https://i.imgur.com/jgIxuG7.png', 350, 160));
collects.append (Sprite ('https://i.imgur.com/jgIxuG7.png', 720, 180));
export var final = TextSprite ('🍉', __kwargtrans__ ({x: 920, y: 240}));
final.py_metatype = 3;
collects.append (final);
export var enemies = [];
export var en01 = TextSprite ('😈', __kwargtrans__ ({x: 200, y: 220}));
en01.y_dir = -(1);
en01.x_dir = 1;
enemies.append (en01);
export var en02 = TextSprite ('👻', __kwargtrans__ ({x: 500, y: 20}));
en02.y_dir = -(1);
en02.x_dir = 1;
enemies.append (en02);
export var en03 = TextSprite ('😾', __kwargtrans__ ({x: 580, y: 20}));
en03.y_dir = -(1);
en03.x_dir = -(0.25);
enemies.append (en03);
export var isFirstTime = true;
export var won = false;
export var Game = graphics.loop (function () {
	graphics.py_clear (0, 0.5, 1.0);
	while (graphics.loadingResources > 0 && isFirstTime) {
		graphics.drawText ('Loading resources..', 0, 0);
		return ;
	}
	isFirstTime = false;
	if (won) {
		graphics.py_clear ();
		graphics.drawText ('YOU WON!', 220, 200);
		graphics.drawText ('Score: ' + str (player.score), 225, 160);
	}
	else if (player.lives > 0) {
		var old_x = player.x;
		var old_y = player.y;
		if (graphics.isKeyPressed (KEY_D) || graphics.isKeyPressed (KEY_V_RIGHT)) {
			player.x += 2;
			player.x_dir = 1;
			player.image = 'https://i.imgur.com/wDa6mLI.png';
		}
		if (graphics.isKeyPressed (KEY_A) || graphics.isKeyPressed (KEY_V_LEFT)) {
			player.x -= 2;
			player.x_dir = -(1);
			player.image = 'https://i.imgur.com/o1GtfiB.png';
		}
		if ((graphics.isKeyPressed (KEY_W) || graphics.isKeyPressed (KEY_V_UP) || graphics.isKeyPressed (KEY_V_FIRE)) && player.can_jump) {
			player.y_dir += 15;
		}
		player.y_dir -= 1;
		player.y += player.y_dir;
		player.can_jump = false;
		for (var wall of walls) {
			if (player.overlaps (wall)) {
				if (player.y_dir > 0) {
					if (old_y + player.getHeight () < wall.y + 1) {
						player.y = wall.y - player.getHeight ();
						player.y_dir = 0;
						if (wall.py_metatype == 2) {
							wall.b += 0.2;
							wall.r -= 0.2;
							if (wall.b >= 1) {
								wall.b = 1;
								wall.r = 0;
								wall.py_metatype = 0;
								collects.append (TextSprite ('🍓', __kwargtrans__ ({x: wall.x - 6, y: wall.y + wall.getHeight () * 2})));
							}
						}
						if (wall.py_metatype == 1) {
							wall.py_metatype = 2;
						}
					}
				}
				if (wall.py_metatype != 1) {
					if (player.y_dir < 0) {
						if (old_y > (wall.y + wall.getHeight ()) - 1) {
							player.y = wall.y + wall.getHeight ();
							player.y_dir = 0;
							player.can_jump = true;
						}
					}
					if (player.x_dir < 0 && old_x > (wall.x + wall.getWidth ()) - 1) {
						player.x = wall.x + wall.getWidth ();
						player.x_dir = 0;
					}
					else if (player.x_dir > 0 && old_x + player.getWidth () < wall.x + 1) {
						player.x = wall.x - player.getWidth ();
						player.x_dir = 0;
					}
				}
			}
			for (var enemy of enemies) {
				if (enemy.overlaps (wall)) {
					if (enemy.x_dir < 0) {
						enemy.x = wall.x + wall.getWidth ();
					}
					else {
						enemy.x = wall.x - enemy.getWidth ();
					}
					enemy.x_dir = -(enemy.x_dir);
				}
			}
		}
		for (var enemy of enemies) {
			enemy.y_dir -= 1;
			enemy.x += enemy.x_dir;
			enemy.y += enemy.y_dir;
		}
		for (var floor of floors) {
			if (player.overlaps (floor) && player.y_dir < 0) {
				player.y = floor.y + floor.getHeight ();
				player.y_dir = 0;
				player.can_jump = true;
			}
			for (var enemy of enemies) {
				if (enemy.overlaps (floor) && enemy.y_dir < 0) {
					enemy.y = floor.y + floor.getHeight ();
					enemy.y_dir = 0;
				}
			}
		}
		var n = 0;
		while (n < len (enemies)) {
			if (player.overlaps (enemies [n])) {
				if (player.y_dir < 0) {
					enemies.py_pop (n);
					player.score += 10;
					player.y_dir = 10;
				}
				else {
					player.lives -= 1;
				}
			}
			n += 1;
		}
		var n = 0;
		while (n < len (collects)) {
			if (player.overlaps (collects [n])) {
				if (collects [n].py_metatype == 3) {
					won = true;
				}
				collects.py_pop (n);
				player.score += 10;
			}
			n += 1;
		}
		if (player.y < 0) {
			player.lives -= 1;
		}
		var offsetX = 0;
		if (player.x > graphics.width / 2) {
			var offsetX = player.x - graphics.width / 2;
		}
		if (player.x > level_width - graphics.width / 2) {
			var offsetX = level_width - graphics.width;
		}
		for (var floor of floors) {
			graphics.drawSprite (floor, offsetX);
		}
		for (var wall of walls) {
			if (wall.py_metatype != 1) {
				graphics.drawSprite (wall, offsetX);
			}
		}
		for (var collect of collects) {
			graphics.drawSprite (collect, offsetX);
		}
		for (var enemy of enemies) {
			graphics.drawSprite (enemy, offsetX);
		}
		graphics.drawSprite (player, offsetX);
		graphics.drawText ('Score: ' + str (player.score), 0, 380);
		graphics.drawText ('Lives: ' + str (player.lives), 440, 380);
	}
	else {
		graphics.drawText ('GAME OVER!', 200, 200, __kwargtrans__ ({r: 1}));
		graphics.stopSound (music);
	}
});

//# sourceMappingURL=mario_clone.map