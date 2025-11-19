---
layout: default
title: Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion
---

# Towards Deploying VLA without Fine-Tuning: Plug-and-Play Inference-Time VLA Policy Steering via Embodied Evolutionary Diffusion
**arXiv**：[2511.14178v1](https://arxiv.org/abs/2511.14178) · [PDF](https://arxiv.org/pdf/2511.14178.pdf)  
**作者**：Zhuo Li, Junjia Liu, Zhipeng Dong, Tao Teng, Quentin Rouxel, Darwin Caldwell, Fei Chen  

**一句话要点**：提出VLA-Pilot方法，实现无需微调的视觉语言动作模型零样本部署。

**关键词**：视觉语言动作模型, 零样本部署, 推理时策略引导, 机器人操作, 即插即用方法

## 3 点简述
- 预训练VLA模型在下游部署时性能显著下降，依赖微调成本高。
- VLA-Pilot为即插即用推理时策略引导方法，无需额外数据或微调。
- 在六项真实世界操作任务中验证，显著提升成功率和泛化能力。

## 摘要（原文）

> Vision-Language-Action (VLA) models have demonstrated significant potential in real-world robotic manipulation. However, pre-trained VLA policies still suffer from substantial performance degradation during downstream deployment. Although fine-tuning can mitigate this issue, its reliance on costly demonstration collection and intensive computation makes it impractical in real-world settings. In this work, we introduce VLA-Pilot, a plug-and-play inference-time policy steering method for zero-shot deployment of pre-trained VLA without any additional fine-tuning or data collection. We evaluate VLA-Pilot on six real-world downstream manipulation tasks across two distinct robotic embodiments, encompassing both in-distribution and out-of-distribution scenarios. Experimental results demonstrate that VLA-Pilot substantially boosts the success rates of off-the-shelf pre-trained VLA policies, enabling robust zero-shot generalization to diverse tasks and embodiments. Experimental videos and code are available at: https://rip4kobe.github.io/vla-pilot/.

