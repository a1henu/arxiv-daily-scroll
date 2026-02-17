---
layout: default
title: WebWorld: A Large-Scale World Model for Web Agent Training
---

# WebWorld: A Large-Scale World Model for Web Agent Training
**arXiv**：[2602.14721v1](https://arxiv.org/abs/2602.14721) · [PDF](https://arxiv.org/pdf/2602.14721.pdf)  
**作者**：Zikai Xiao, Jianhong Tu, Chuhang Zou, Yuxin Zuo, Zhi Li, Peng Wang, Bowen Yu, Fei Huang, Junyang Lin, Zuozhu Liu  

**一句话要点**：提出WebWorld大规模开放网络模拟器以解决网络代理训练中的数据限制问题

**关键词**：网络模拟器, 大规模训练, 世界模型, 开放网络交互, 跨领域泛化

## 3 点简述
- 网络代理训练受限于真实网络延迟、速率限制和安全风险，需要大规模轨迹数据
- WebWorld通过可扩展数据管道训练100万+开放网络交互，支持推理、多格式数据和30+步长时模拟
- 在WebWorld-Bench上模拟性能媲美Gemini-3-Pro，Qwen3-14B训练后WebArena性能提升9.2%，并展示跨领域泛化能力

## 摘要（原文）

> Web agents require massive trajectories to generalize, yet real-world training is constrained by network latency, rate limits, and safety risks. We introduce \textbf{WebWorld} series, the first open-web simulator trained at scale. While existing simulators are restricted to closed environments with thousands of trajectories, WebWorld leverages a scalable data pipeline to train on 1M+ open-web interactions, supporting reasoning, multi-format data, and long-horizon simulations of 30+ steps. For intrinsic evaluation, we introduce WebWorld-Bench with dual metrics spanning nine dimensions, where WebWorld achieves simulation performance comparable to Gemini-3-Pro. For extrinsic evaluation, Qwen3-14B trained on WebWorld-synthesized trajectories improves by +9.2\% on WebArena, reaching performance comparable to GPT-4o. WebWorld enables effective inference-time search, outperforming GPT-5 as a world model. Beyond web simulation, WebWorld exhibits cross-domain generalization to code, GUI, and game environments, providing a replicable recipe for world model construction.

