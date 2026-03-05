---
layout: default
title: Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
---

# Pretrained Vision-Language-Action Models are Surprisingly Resistant to Forgetting in Continual Learning
**arXiv**：[2603.03818v1](https://arxiv.org/abs/2603.03818) · [PDF](https://arxiv.org/pdf/2603.03818.pdf)  
**作者**：Huihan Liu, Changyeon Kim, Bo Liu, Minghuan Liu, Yuke Zhu  

**一句话要点**：发现预训练视觉-语言-动作模型在持续学习中具有强抗遗忘性，简单经验回放即可有效学习新技能

**关键词**：持续学习, 视觉-语言-动作模型, 经验回放, 抗遗忘性, 机器人策略学习, 预训练模型

## 3 点简述
- 研究持续学习中机器人策略遗忘问题，对比预训练VLA模型与从头训练小模型的抗遗忘能力
- 发现预训练VLA模型抗遗忘性强，简单经验回放即可实现低遗忘甚至零遗忘，并保持前向学习能力
- 分析表明预训练是关键，模型能保留先验知识，通过微调快速恢复遗忘技能，改变持续学习动态

## 摘要（原文）

> Continual learning is a long-standing challenge in robot policy learning, where a policy must acquire new skills over time without catastrophically forgetting previously learned ones. While prior work has extensively studied continual learning in relatively small behavior cloning (BC) policy models trained from scratch, its behavior in modern large-scale pretrained Vision-Language-Action (VLA) models remains underexplored. In this work, we found that pretrained VLAs are remarkably resistant to forgetting compared with smaller policy models trained from scratch. Simple Experience Replay (ER) works surprisingly well on VLAs, sometimes achieving zero forgetting even with a small replay data size. Our analysis reveals that pretraining plays a critical role in downstream continual learning performance: large pretrained models mitigate forgetting with a small replay buffer size while maintaining strong forward learning capabilities. Furthermore, we found that VLAs can retain relevant knowledge from prior tasks despite performance degradation during learning new tasks. This knowledge retention enables rapid recovery of seemingly forgotten skills through finetuning. Together, these insights imply that large-scale pretraining fundamentally changes the dynamics of continual learning, enabling models to continually acquire new skills over time with simple replay. Code and more information can be found at https://ut-austin-rpl.github.io/continual-vla

