---
layout: default
title: World Models Can Leverage Human Videos for Dexterous Manipulation
---

# World Models Can Leverage Human Videos for Dexterous Manipulation
**arXiv**：[2512.13644v1](https://arxiv.org/abs/2512.13644) · [PDF](https://arxiv.org/pdf/2512.13644.pdf)  
**作者**：Raktim Gautam Goswami, Amir Bar, David Fan, Tsung-Yen Yang, Gaoyue Zhou, Prashanth Krishnamurthy, Michael Rabbat, Farshad Khorrami, Yann LeCun  

**一句话要点**：提出DexWM世界模型，利用人类视频解决灵巧操作预测问题。

**关键词**：灵巧操作, 世界模型, 视频训练, 手部一致性损失, 零样本泛化

## 3 点简述
- 核心问题：灵巧操作需理解手部细微运动对物体的接触影响，但数据集稀缺。
- 方法要点：训练世界模型预测潜在状态，引入手部一致性损失提升精细操作能力。
- 实验或效果：在未见技能上零样本泛化，部署机器人任务中超越Diffusion Policy。

## 摘要（原文）

> Dexterous manipulation is challenging because it requires understanding how subtle hand motion influences the environment through contact with objects. We introduce DexWM, a Dexterous Manipulation World Model that predicts the next latent state of the environment conditioned on past states and dexterous actions. To overcome the scarcity of dexterous manipulation datasets, DexWM is trained on over 900 hours of human and non-dexterous robot videos. To enable fine-grained dexterity, we find that predicting visual features alone is insufficient; therefore, we introduce an auxiliary hand consistency loss that enforces accurate hand configurations. DexWM outperforms prior world models conditioned on text, navigation, and full-body actions, achieving more accurate predictions of future states. DexWM also demonstrates strong zero-shot generalization to unseen manipulation skills when deployed on a Franka Panda arm equipped with an Allegro gripper, outperforming Diffusion Policy by over 50% on average in grasping, placing, and reaching tasks.

