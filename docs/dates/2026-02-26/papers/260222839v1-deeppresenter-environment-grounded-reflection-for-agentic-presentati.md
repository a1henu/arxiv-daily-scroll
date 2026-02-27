---
layout: default
title: DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation
---

# DeepPresenter: Environment-Grounded Reflection for Agentic Presentation Generation
**arXiv**：[2602.22839v1](https://arxiv.org/abs/2602.22839) · [PDF](https://arxiv.org/pdf/2602.22839.pdf)  
**作者**：Hao Zheng, Guozhao Mo, Xinru Yan, Qianhao Yuan, Wenkai Zhang, Xuanang Chen, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun  

**一句话要点**：提出DeepPresenter框架，通过环境感知反思解决自适应演示生成问题。

**关键词**：演示生成, 环境感知反思, 自适应代理, 长时程优化, 幻灯片渲染

## 3 点简述
- 核心问题：现有演示生成代理依赖预定义流程和固定模板，缺乏自适应性和迭代优化能力。
- 方法要点：采用环境感知反思机制，基于感知到的幻灯片状态进行规划和修订，支持长时程优化。
- 实验或效果：在多样化演示生成场景评估中达到最优性能，9B模型在低成本下保持高竞争力。

## 摘要（原文）

> Presentation generation requires deep content research, coherent visual design, and iterative refinement based on observation. However, existing presentation agents often rely on predefined workflows and fixed templates. To address this, we present DeepPresenter, an agentic framework that adapts to diverse user intents, enables effective feedback-driven refinement, and generalizes beyond a scripted pipeline. Specifically, DeepPresenter autonomously plans, renders, and revises intermediate slide artifacts to support long-horizon refinement with environmental observations. Furthermore, rather than relying on self-reflection over internal signals (e.g., reasoning traces), our environment-grounded reflection conditions the generation process on perceptual artifact states (e.g., rendered slides), enabling the system to identify and correct presentation-specific issues during execution. Results on the evaluation set covering diverse presentation-generation scenarios show that DeepPresenter achieves state-of-the-art performance, and the fine-tuned 9B model remains highly competitive at substantially lower cost. Our project is available at: https://github.com/icip-cas/PPTAgent

