---
layout: default
title: CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning
---

# CGL: Advancing Continual GUI Learning via Reinforcement Fine-Tuning
**arXiv**：[2603.02951v1](https://arxiv.org/abs/2603.02951) · [PDF](https://arxiv.org/pdf/2603.02951.pdf)  
**作者**：Zhenquan Yao, Zitong Huang, Yihan Zeng, Jianhua Han, Hang Xu, Chun-Mei Feng, Jianwei Ma, Wangmeng Zuo  

**一句话要点**：提出CGL框架，通过强化微调平衡适应与遗忘，解决GUI持续学习问题。

**关键词**：GUI持续学习, 强化微调, 梯度手术, 多模态大语言模型, Android基准

## 3 点简述
- 核心问题：GUI应用频繁更新导致持续学习中适应新任务时遗忘旧任务。
- 方法要点：动态调整SFT与RL权重，引入梯度手术策略减少梯度冲突。
- 实验或效果：在AndroidControl-CL基准上验证了CGL在持续学习场景中的有效性。

## 摘要（原文）

> Graphical User Interface (GUI) Agents, benefiting from recent advances in multimodal large language models (MLLM), have achieved significant development. However, due to the frequent updates of GUI applications, adapting to new tasks without forgetting old tasks in GUI continual learning remains an open problem. In this work, we reveal that while Supervised Fine-Tuning (SFT) facilitates fast adaptation, it often triggers knowledge overwriting, whereas Reinforcement Learning (RL) demonstrates an inherent resilience that shields prior interaction logic from erasure. Based on this insight, we propose a \textbf{C}ontinual \textbf{G}UI \textbf{L}earning (CGL) framework that dynamically balances adaptation efficiency and skill retention by enhancing the synergy between SFT and RL. Specifically, we introduce an SFT proportion adjustment mechanism guided by policy entropy to dynamically control the weight allocation between the SFT and RL training phases. To resolve explicit gradient interference, we further develop a specialized gradient surgery strategy. By projecting exploratory SFT gradients onto GRPO-based anchor gradients, our method explicitly clips the components of SFT gradients that conflict with GRPO. On top of that, we establish an AndroidControl-CL benchmark, which divides GUI applications into distinct task groups to effectively simulate and evaluate the performance of continual GUI learning. Experimental results demonstrate the effectiveness of our proposed CGL framework across continual learning scenarios. The benchmark, code, and model will be made publicly available.

