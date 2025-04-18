# MachineLearningTetris

This fork has the single-action DQN with video recording capability and wandb integration. ungrouped_dqn_train is the bread and butter of this model. The work in progress is the train_cnn_test_with_ruleBasedPrior.py file, where we try to fill the relay buffer with a high-quality rule-based algorithmic approach.


TODO: follow the principles of: https://codemyroad.wordpress.com/2013/04/14/tetris-ai-the-near-perfect-player/

Apply more specific rewards for actions that are not tetromino placements

Get the relay buffer filled by either :
\t-running 2 seperate render mode envs at the same time with the same seed
\t-use the pretrained model from last time we saved and ran validation on
\t-somehow have the rule-based model accept rgb.

Also make sure the model has higher exploration depth

Next step: geentic algorithm for rapid advancement; require parallel computing.
