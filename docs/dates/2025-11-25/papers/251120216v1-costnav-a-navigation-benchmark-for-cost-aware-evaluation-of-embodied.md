---
layout: default
title: CostNav: A Navigation Benchmark for Cost-Aware Evaluation of Embodied Agents
---

# CostNav: A Navigation Benchmark for Cost-Aware Evaluation of Embodied Agents
**arXiv**：[2511.20216v1](https://arxiv.org/abs/2511.20216) · [PDF](https://arxiv.org/pdf/2511.20216.pdf)  
**作者**：Haebin Seong, Sungmin Kim, Minchan Kim, Yongjun Cho, Myunchul Joe, Suhwan Choi, Jaeyoon Jung, Jiyong Youn, Yoonshik Kim, Samwoo Seong, Yubeen Park, Youngjae Yu, Yunsung Lee  

**一句话要点**：提出CostNav导航基准，通过成本收益分析评估具身代理的商业可行性。

**关键词**：具身代理导航, 成本收益分析, 商业可行性评估, 微观导航测试台, 碰撞避免优化

## 3 点简述
- 现有导航基准忽视经济可行性，影响自主配送机器人的商业部署。
- 引入微观导航经济测试台，建模硬件、能源、维护等成本与交付收入。
- 实验显示基线方法在SLA合规43.0%时仍亏损，突出碰撞避免为优化关键。

## 摘要（原文）

> Existing navigation benchmarks focus on task success metrics while overlooking economic viability -- critical for commercial deployment of autonomous delivery robots. We introduce \emph{CostNav}, a \textbf{Micro-Navigation Economic Testbed} that evaluates embodied agents through comprehensive cost-revenue analysis aligned with real-world business operations. CostNav models the complete economic lifecycle including hardware, training, energy, maintenance costs, and delivery revenue with service-level agreements, using industry-derived parameters. \textbf{To our knowledge, CostNav is the first work to quantitatively expose the gap between navigation research metrics and commercial viability}, revealing that optimizing for task success fundamentally differs from optimizing for economic deployment. Our cost model uses parameters derived from industry data sources (energy rates, delivery service pricing), and we project from a reduced-scale simulation to realistic deliveries. Under this projection, the baseline achieves 43.0\% SLA compliance but is \emph{not} commercially viable: yielding a loss of \$30.009 per run with no finite break-even point, because operating costs are dominated by collision-induced maintenance, which accounts for 99.7\% of per-run costs and highlights collision avoidance as a key optimization target. We demonstrate a learning-based on-device navigation baseline and establish a foundation for evaluating rule-based navigation, imitation learning, and cost-aware RL training. CostNav bridges the gap between navigation research and commercial deployment, enabling data-driven decisions about economic trade-offs across navigation paradigms.

