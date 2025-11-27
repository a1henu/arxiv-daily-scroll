---
layout: default
title: CAHS-Attack: CLIP-Aware Heuristic Search Attack Method for Stable Diffusion
---

# CAHS-Attack: CLIP-Aware Heuristic Search Attack Method for Stable Diffusion
**arXiv**：[2511.21180v1](https://arxiv.org/abs/2511.21180) · [PDF](https://arxiv.org/pdf/2511.21180.pdf)  
**作者**：Shuhan Xia, Jing Dai, Hui Ouyang, Yadong Shang, Dongxiao Zhao, Peipei Li  

**一句话要点**：提出CAHS-Attack方法以增强对Stable Diffusion模型的对抗性攻击能力

**关键词**：对抗性攻击, 扩散模型, CLIP编码器, 启发式搜索, 文本到图像生成

## 3 点简述
- 扩散模型易受对抗提示攻击，现有方法依赖白盒访问或手工工程，实际部署受限
- 结合蒙特卡洛树搜索和约束遗传算法，优化后缀提示，实现高效局部搜索
- 实验显示在多种语义提示下达到最优攻击效果，揭示CLIP文本编码器固有脆弱性

## 摘要（原文）

> Diffusion models exhibit notable fragility when faced with adversarial prompts, and strengthening attack capabilities is crucial for uncovering such vulnerabilities and building more robust generative systems. Existing works often rely on white-box access to model gradients or hand-crafted prompt engineering, which is infeasible in real-world deployments due to restricted access or poor attack effect. In this paper, we propose CAHS-Attack , a CLIP-Aware Heuristic Search attack method. CAHS-Attack integrates Monte Carlo Tree Search (MCTS) to perform fine-grained suffix optimization, leveraging a constrained genetic algorithm to preselect high-potential adversarial prompts as root nodes, and retaining the most semantically disruptive outcome at each simulation rollout for efficient local search. Extensive experiments demonstrate that our method achieves state-of-the-art attack performance across both short and long prompts of varying semantics. Furthermore, we find that the fragility of SD models can be attributed to the inherent vulnerability of their CLIP-based text encoders, suggesting a fundamental security risk in current text-to-image pipelines.

