---
layout: default
title: White-Box Op-Amp Design via Human-Mimicking Reasoning
---

# White-Box Op-Amp Design via Human-Mimicking Reasoning
**arXiv**：[2601.21321v1](https://arxiv.org/abs/2601.21321) · [PDF](https://arxiv.org/pdf/2601.21321.pdf)  
**作者**：Zihao Chen, Jiayin Wang, Ziyi Sun, Ji Zhuang, Jinyi Shen, Xiaoyue Ke, Li Shang, Xuan Zeng, Fan Yang  

**一句话要点**：提出White-Op框架，基于大语言模型代理的拟人推理实现可解释的运算放大器参数设计。

**关键词**：运算放大器设计, 可解释人工智能, 大语言模型代理, 符号化极点零点调节, 闭式优化问题, 晶体管级映射

## 3 点简述
- 核心问题：运算放大器参数设计通常依赖黑盒方法，缺乏可解释性和可靠性。
- 方法要点：通过引入假设约束，建立假设-验证-决策的迭代工作流，将设计转化为闭式数学优化问题。
- 实验或效果：在9种拓扑上验证，相比黑盒基线失败5种，White-Op理论预测误差仅8.52%，所有拓扑晶体管级映射后功能保持。

## 摘要（原文）

> This brief proposes \emph{White-Op}, an interpretable operational amplifier (op-amp) parameter design framework based on the human-mimicking reasoning of large-language-model agents. We formalize the implicit human reasoning mechanism into explicit steps of \emph{\textbf{introducing hypothetical constraints}}, and develop an iterative, human-like \emph{\textbf{hypothesis-verification-decision}} workflow. Specifically, the agent is guided to introduce hypothetical constraints to derive and properly regulate positions of symbolically tractable poles and zeros, thus formulating a closed-form mathematical optimization problem, which is then solved programmatically and verified via simulation. Theory-simulation result analysis guides the decision-making for refinement. Experiments on 9 op-amp topologies show that, unlike the uninterpretable black-box baseline which finally fails in 5 topologies, White-Op achieves reliable, interpretable behavioral-level designs with only 8.52\% theoretical prediction error and the design functionality retains after transistor-level mapping for all topologies. White-Op is open-sourced at \textcolor{blue}{https://github.com/zhchenfdu/whiteop}.

