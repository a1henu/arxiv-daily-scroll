---
layout: default
title: BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks
---

# BugSweeper: Function-Level Detection of Smart Contract Vulnerabilities Using Graph Neural Networks
**arXiv**：[2512.09385v1](https://arxiv.org/abs/2512.09385) · [PDF](https://arxiv.org/pdf/2512.09385.pdf)  
**作者**：Uisang Lee, Changhoon Chung, Junmo Lee, Soo-Mook Moon  

**一句话要点**：提出BugSweeper，基于图神经网络在函数级别检测智能合约漏洞，无需手动规则。

**关键词**：智能合约安全, 图神经网络, 漏洞检测, 函数级分析, 抽象语法图

## 3 点简述
- 核心问题：现有方法依赖专家设计的规则预处理，可能忽略关键上下文，限制对新威胁的适应性。
- 方法要点：将Solidity函数表示为函数级抽象语法图，结合两阶段图神经网络进行噪声过滤和高层推理。
- 实验或效果：在真实合约上实验显示，BugSweeper显著优于所有最先进的检测方法。

## 摘要（原文）

> The rapid growth of Ethereum has made it more important to quickly and accurately detect smart contract vulnerabilities. While machine-learning-based methods have shown some promise, many still rely on rule-based preprocessing designed by domain experts. Rule-based preprocessing methods often discard crucial context from the source code, potentially causing certain vulnerabilities to be overlooked and limiting adaptability to newly emerging threats. We introduce BugSweeper, an end-to-end deep learning framework that detects vulnerabilities directly from the source code without manual engineering. BugSweeper represents each Solidity function as a Function-Level Abstract Syntax Graph (FLAG), a novel graph that combines its Abstract Syntax Tree (AST) with enriched control-flow and data-flow semantics. Then, our two-stage Graph Neural Network (GNN) analyzes these graphs. The first-stage GNN filters noise from the syntax graphs, while the second-stage GNN conducts high-level reasoning to detect diverse vulnerabilities. Extensive experiments on real-world contracts show that BugSweeper significantly outperforms all state-of-the-art detection methods. By removing the need for handcrafted rules, our approach offers a robust, automated, and scalable solution for securing smart contracts without any dependence on security experts.

