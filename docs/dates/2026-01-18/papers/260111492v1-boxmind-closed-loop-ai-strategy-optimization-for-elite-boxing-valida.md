---
layout: default
title: BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics
---

# BoxMind: Closed-loop AI strategy optimization for elite boxing validated in the 2024 Olympics
**arXiv**：[2601.11492v1](https://arxiv.org/abs/2601.11492) · [PDF](https://arxiv.org/pdf/2601.11492.pdf)  
**作者**：Kaiwen Wang, Kaili Zheng, Rongrong Deng, Qingmin Fan, Milin Zhang, Zongrui Li, Xuesi Zhou, Bo Han, Liren Chen, Chenyi Guo, Ji Wu  

**一句话要点**：提出BoxMind闭环AI系统，通过解析拳击视频为战术指标并建模预测，以优化精英拳击策略，在2024奥运会验证。

**关键词**：拳击战术分析, 视频解析, 图预测模型, 闭环AI系统, 体育决策支持

## 3 点简述
- 核心问题：拳击等格斗运动因动作动态复杂和缺乏结构化战术表示，AI分析发展不足。
- 方法要点：定义原子击打事件，解析视频为18个战术指标，结合图模型和可学习嵌入预测比赛结果。
- 实验或效果：预测模型在测试集准确率69.8%，奥运比赛87.5%；闭环部署助力中国队获3金2银，策略建议媲美专家。

## 摘要（原文）

> Competitive sports require sophisticated tactical analysis, yet combat disciplines like boxing remain underdeveloped in AI-driven analytics due to the complexity of action dynamics and the lack of structured tactical representations. To address this, we present BoxMind, a closed-loop AI expert system validated in elite boxing competition. By defining atomic punch events with precise temporal boundaries and spatial and technical attributes, we parse match footage into 18 hierarchical technical-tactical indicators. We then propose a graph-based predictive model that fuses these explicit technical-tactical profiles with learnable, time-variant latent embeddings to capture the dynamics of boxer matchups. Modeling match outcome as a differentiable function of technical-tactical indicators, we turn winning probability gradients into executable tactical adjustments. Experiments show that the outcome prediction model achieves state-of-the-art performance, with 69.8% accuracy on BoxerGraph test set and 87.5% on Olympic matches. Using this predictive model as a foundation, the system generates strategic recommendations that demonstrate proficiency comparable to human experts. BoxMind is validated through a closed-loop deployment during the 2024 Paris Olympics, directly contributing to the Chinese National Team's historic achievement of three gold and two silver medals. BoxMind establishes a replicable paradigm for transforming unstructured video data into strategic intelligence, bridging the gap between computer vision and decision support in competitive sports.

