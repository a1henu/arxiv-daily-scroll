---
layout: default
title: Privacy-Preserving Synthetic Dataset of Individual Daily Trajectories for City-Scale Mobility Analytics
---

# Privacy-Preserving Synthetic Dataset of Individual Daily Trajectories for City-Scale Mobility Analytics
**arXiv**：[2512.17239v1](https://arxiv.org/abs/2512.17239) · [PDF](https://arxiv.org/pdf/2512.17239.pdf)  
**作者**：Jun'ichi Ozaki, Ryosuke Susuta, Takuhiro Moriyama, Yohei Shida  

**一句话要点**：提出隐私保护合成轨迹数据集方法，以聚合输入重建个体日常轨迹，支持城市尺度移动分析。

**关键词**：隐私保护, 合成数据, 移动轨迹, 多目标优化, 城市移动分析

## 3 点简述
- 核心问题：个体GPS轨迹因重识别风险难以共享，聚合数据如OD矩阵无法捕捉日常移动行为细节。
- 方法要点：结合OD流、停留-出行时间分位数和访问位置数分布定律，通过多目标优化生成合成轨迹。
- 实验或效果：在东京和福冈验证，合成数据高保真重现行为分布，OD一致性偏差在自然波动范围内。

## 摘要（原文）

> Urban mobility data are indispensable for urban planning, transportation demand forecasting, pandemic modeling, and many other applications; however, individual mobile phone-derived Global Positioning System traces cannot generally be shared with third parties owing to severe re-identification risks. Aggregated records, such as origin-destination (OD) matrices, offer partial insights but fail to capture the key behavioral properties of daily human movement, limiting realistic city-scale analyses.
>   This study presents a privacy-preserving synthetic mobility dataset that reconstructs daily trajectories from aggregated inputs. The proposed method integrates OD flows with two complementary behavioral constraints: (1) dwell-travel time quantiles that are available only as coarse summary statistics and (2) the universal law for the daily distribution of the number of visited locations. Embedding these elements in a multi-objective optimization framework enables the reproduction of realistic distributions of human mobility while ensuring that no personal identifiers are required.
>   The proposed framework is validated in two contrasting regions of Japan: (1) the 23 special wards of Tokyo, representing a dense metropolitan environment; and (2) Fukuoka Prefecture, where urban and suburban mobility patterns coexist. The resulting synthetic mobility data reproduce dwell-travel time and visit frequency distributions with high fidelity, while deviations in OD consistency remain within the natural range of daily fluctuations.
>   The results of this study establish a practical synthesis pathway under real-world constraints, providing governments, urban planners, and industries with scalable access to high-resolution mobility data for reliable analytics without the need for sensitive personal records, and supporting practical deployments in policy and commercial domains.

