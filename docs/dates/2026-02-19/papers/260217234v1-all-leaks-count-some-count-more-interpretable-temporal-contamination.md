---
layout: default
title: All Leaks Count, Some Count More: Interpretable Temporal Contamination Detection in LLM Backtesting
---

# All Leaks Count, Some Count More: Interpretable Temporal Contamination Detection in LLM Backtesting
**arXiv**：[2602.17234v1](https://arxiv.org/abs/2602.17234) · [PDF](https://arxiv.org/pdf/2602.17234.pdf)  
**作者**：Zeyu Zhang, Ryan Chen, Bradly C. Stadie  

**一句话要点**：提出Shapley-DCLR和TimeSPEC框架，以检测和减少LLM回溯测试中的时间知识泄露。

**关键词**：时间知识泄露, 回溯测试, Shapley值, 声明级验证, LLM评估

## 3 点简述
- 核心问题：LLM在训练中可能泄露截止日期后的知识，影响回溯测试的有效性。
- 方法要点：通过分解模型推理为原子声明，应用Shapley值量化泄露贡献，并开发TimeSPEC进行主动过滤。
- 实验效果：在多个任务中验证了泄露问题，TimeSPEC能降低泄露率同时保持性能。

## 摘要（原文）

> To evaluate whether LLMs can accurately predict future events, we need the ability to \textit{backtest} them on events that have already resolved. This requires models to reason only with information available at a specified past date. Yet LLMs may inadvertently leak post-cutoff knowledge encoded during training, undermining the validity of retrospective evaluation. We introduce a claim-level framework for detecting and quantifying this \emph{temporal knowledge leakage}. Our approach decomposes model rationales into atomic claims and categorizes them by temporal verifiability, then applies \textit{Shapley values} to measure each claim's contribution to the prediction. This yields the \textbf{Shapley}-weighted \textbf{D}ecision-\textbf{C}ritical \textbf{L}eakage \textbf{R}ate (\textbf{Shapley-DCLR}), an interpretable metric that captures what fraction of decision-driving reasoning derives from leaked information. Building on this framework, we propose \textbf{Time}-\textbf{S}upervised \textbf{P}rediction with \textbf{E}xtracted \textbf{C}laims (\textbf{TimeSPEC}), which interleaves generation with claim verification and regeneration to proactively filter temporal contamination -- producing predictions where every supporting claim can be traced to sources available before the cutoff date. Experiments on 350 instances spanning U.S. Supreme Court case prediction, NBA salary estimation, and stock return ranking reveal substantial leakage in standard prompting baselines. TimeSPEC reduces Shapley-DCLR while preserving task performance, demonstrating that explicit, interpretable claim-level verification outperforms prompt-based temporal constraints for reliable backtesting.

