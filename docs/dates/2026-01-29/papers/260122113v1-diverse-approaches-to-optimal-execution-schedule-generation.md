---
layout: default
title: Diverse Approaches to Optimal Execution Schedule Generation
---

# Diverse Approaches to Optimal Execution Schedule Generation
**arXiv**：[2601.22113v1](https://arxiv.org/abs/2601.22113) · [PDF](https://arxiv.org/pdf/2601.22113.pdf)  
**作者**：Robert de Witt, Mikko S. Pakkanen  

**一句话要点**：提出应用MAP-Elites质量多样性算法于交易执行，生成基于流动性和波动性条件的多样化策略组合。

**关键词**：交易执行, 质量多样性算法, MAP-Elites, 强化学习, 模拟环境, 策略组合

## 3 点简述
- 核心问题：传统交易执行策略可能无法适应不同市场条件，需开发能生成多样化、条件专用策略的方法。
- 方法要点：首次将MAP-Elites算法应用于交易执行，生成按流动性和波动性索引的专用策略组合，而非单一最优策略。
- 实验或效果：专用策略在特定行为生态位内实现8-10%性能提升，CNN架构在模拟环境中优于行业基线，验证了模拟真实性和方法潜力。

## 摘要（原文）

> We present the first application of MAP-Elites, a quality-diversity algorithm, to trade execution. Rather than searching for a single optimal policy, MAP-Elites generates a diverse portfolio of regime-specialist strategies indexed by liquidity and volatility conditions. Individual specialists achieve 8-10% performance improvements within their behavioural niches, while other cells show degradation, suggesting opportunities for ensemble approaches that combine improved specialists with the baseline PPO policy. Results indicate that quality-diversity methods offer promise for regime-adaptive execution, though substantial computational resources per behavioural cell may be required for robust specialist development across all market conditions. To ensure experimental integrity, we develop a calibrated Gymnasium environment focused on order scheduling rather than tactical placement decisions. The simulator features a transient impact model with exponential decay and square-root volume scaling, fit to 400+ U.S. equities with R^2>0.02 out-of-sample. Within this environment, two Proximal Policy Optimization architectures - both MLP and CNN feature extractors - demonstrate substantial improvements over industry baselines, with the CNN variant achieving 2.13 bps arrival slippage versus 5.23 bps for VWAP on 4,900 out-of-sample orders ($21B notional). These results validate both the simulation realism and provide strong single-policy baselines for quality-diversity methods.

