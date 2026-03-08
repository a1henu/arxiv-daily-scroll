---
layout: default
title: Poisoning the Inner Prediction Logic of Graph Neural Networks for Clean-Label Backdoor Attacks
---

# Poisoning the Inner Prediction Logic of Graph Neural Networks for Clean-Label Backdoor Attacks
**arXiv**：[2603.05004v1](https://arxiv.org/abs/2603.05004) · [PDF](https://arxiv.org/pdf/2603.05004.pdf)  
**作者**：Yuxiang Zhang, Bin Ma, Enyan Dai  

**一句话要点**：提出BA-Logic以解决图神经网络在干净标签设置下的后门攻击问题

**关键词**：图神经网络, 后门攻击, 干净标签, 逻辑毒化, 节点选择, 触发器生成

## 3 点简述
- 核心问题：现有图后门攻击在训练标签不可修改的干净标签设置下失效，因无法毒化模型内部预测逻辑
- 方法要点：通过协调毒化节点选择器和逻辑毒化触发器生成器，毒化GNN内部预测逻辑，使触发器对预测重要
- 实验或效果：在真实数据集上实验显示，BA-Logic有效提升攻击成功率，超越现有方法

## 摘要（原文）

> Graph Neural Networks (GNNs) have achieved remarkable results in various tasks. Recent studies reveal that graph backdoor attacks can poison the GNN model to predict test nodes with triggers attached as the target class. However, apart from injecting triggers to training nodes, these graph backdoor attacks generally require altering the labels of trigger-attached training nodes into the target class, which is impractical in real-world scenarios. In this work, we focus on the clean-label graph backdoor attack, a realistic but understudied topic where training labels are not modifiable. According to our preliminary analysis, existing graph backdoor attacks generally fail under the clean-label setting. Our further analysis identifies that the core failure of existing methods lies in their inability to poison the prediction logic of GNN models, leading to the triggers being deemed unimportant for prediction. Therefore, we study a novel problem of effective clean-label graph backdoor attacks by poisoning the inner prediction logic of GNN models. We propose BA-Logic to solve the problem by coordinating a poisoned node selector and a logic-poisoning trigger generator. Extensive experiments on real-world datasets demonstrate that our method effectively enhances the attack success rate and surpasses state-of-the-art graph backdoor attack competitors under clean-label settings. Our code is available at https://anonymous.4open.science/r/BA-Logic

