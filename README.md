# Web3 Bug Bounty Programs — Verified Directory

A curated directory of **active Web3 bug bounty programs** where every entry
was actually checked against its live program page. The differentiator vs.
stale aggregator lists: each program carries a **last-verified date**, and any
figure that could not be confirmed says so instead of being invented.

> **Verification standard:** a program is listed only if its program page (or
> the project's own docs/repo) was read live. Reward figures come from that
> page or from the maintainer's own survey notes. Anything unconfirmed is
> marked "check program page". See [CONTRIBUTING.md](CONTRIBUTING.md).

## How to use this list

- **Start with Active, no fee** — these cost $0 to file and have no gate.
- **Gated** programs are live, but filing costs a fee, a stake, reputation
  points, or a platform verification step. Read the notes before spending.
- **Closed / Paused / Dead** are kept so you don't waste time on programs
  aggregators still show as active.
- **Always re-check the program page before hunting.** Terms, scope, and
  reward tiers change; the last-verified date tells you how fresh each row is.

## Active — no fee, no gate

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|

| [Across](https://docs.across.to/introduction/bug-bounty) | Self-hosted | $250 – $1M | No | none | [Across bridge contracts (HubPool, SpokePool, adapters, verifiers)](https://github.com/across-protocol/contracts) | 2026-11-19 |
| [Relay](https://docs.relay.link/security/bounties) | Self-hosted | $500 – $100k | Yes | none | [Relay bridge, Relay Chain, solvers, executors, oracles](https://github.com/relayprotocol) | 2026-11-19 |
| [Marginfi](https://github.com/0dotxyz/marginfi-v2) | Self-hosted | $10k – $500k | No | none | [marginfi-v2 Solana lending program, cross-venue banks, SDK](https://github.com/0dotxyz/marginfi-v2) | 2026-11-19 |
| [Venus](https://bugbounty.bnbchain.org) | BNB Chain Bug Bounty (HackenProof partner program) | $300 – $150k | Yes | none | [Venus Core Pool, Liquidity Hub, spoke markets, VAI (BSC)](https://github.com/VenusProtocol) | 2026-11-19 |
| [ListaDAO](https://bugbounty.bnbchain.org/scope-policy?project=1) | BNB Chain Bug Bounty (HackenProof partner program) | $300 – $150k | Yes | none | [lisUSD CDP, staking, Moolah vaults, StableSwap, Credit, oracles (BSC, 92-contract scope table)](https://github.com/lista-dao) | 2026-11-19 |
| [Valantis STEX](https://r.xyz/bug-bounty/programs/valantis-stex) | Remedy | up to $200k | No | none | [STEXAMM + stHYPEWithdrawalModule only (HyperEVM, chain 999)](https://github.com/ValantisLabs/valantis-stex) | 2026-11-20 |
| [Squads V4](https://github.com/Squads-Protocol/v4) | Self-hosted | $10k – $300k | No | none | [Squads V4 multisig program (Solana) only](https://github.com/Squads-Protocol/v4) | 2026-11-20 |
| [AUTOfinance (Tokemak)](https://r.xyz/bug-bounty/programs/tokemak) | Remedy | $25k – $125k | No | none | [Tokemak v2-core-pub /src (excl. Maverick, /external, /interfaces, /lens, LiquidationExecutor, /staking)](https://github.com/Tokemak/v2-core-pub) | 2026-11-20 |
| [UFarm Digital](https://r.xyz/bug-bounty/programs/ufarm-digital) | Remedy | up to $100k | No | none | [UFarm-EVM-Contracts contracts/ (ETH + Arbitrum)](https://github.com/UFarmDigital/UFarm-EVM-Contracts) | 2026-11-20 |
| [BOB](https://r.xyz/bug-bounty/programs/bob) | Remedy | up to $250k | Yes | none | [BOB L1/L2 contracts (Proxy Admin, Batcher, Proposer, Challenger, Guardian, Bitcoin SPV utils, Relays, Token/Staking)](https://github.com/bob-collective/bob) | 2026-11-20 |
| [Boba Network](https://r.xyz/bug-bounty/programs/boba-network) | Remedy | up to $100k | Yes | none | [Only 5 Proxy__LightBridge contracts (ETH, Boba, OP, Arbitrum deployments)](https://github.com/bobanetwork/boba) | 2026-11-20 |
| [PancakeSwap](https://r.xyz/bug-bounty/programs/pancakeswap) | Remedy | $20k – $1M | No | none | [PancakeSwap V2/V3/Infinity AMM contracts and periphery](https://github.com/pancakeswap/pancake-v3-contracts) | 2026-11-20 |
| [Arc (Circle)](https://hackerone.com/arc-bbp) | HackerOne | $20k – $1M | Unknown | none | [Arc chain, CCTP bridge (EVM + Solana + Noble + Starknet), Gateway, CPN, xReserve](https://github.com/circlefin) | 2026-11-19 |
| [Stellar](https://hackerone.com/stellar) | HackerOne | $0 – $250k | Yes | none | [All open-source repos under the stellar GitHub org + stellar.org web properties; carveout for stellar-core and Soroban (Rust)](https://github.com/stellar) | 2026-11-19 |
| [Chainlink](https://hackerone.com/chainlink) | HackerOne | up to $100k | Unknown | none | [chainlink-evm + chainlink-solana contracts (Data Feeds, VRF, Automation, Functions), Go node, staking v0.1](https://github.com/smartcontractkit/chainlink) | 2026-11-19 |
| [Anchor framework](https://github.com/arcium-hq/anchor) | Self-hosted | $100 – $117.6k | Yes | none | [Anchor framework code only (Solana) — ownership/discriminator/memory-safety bypasses](https://github.com/arcium-hq/anchor) | 2026-11-19 |
| [ERC-4337 Account Abstraction](https://hackenproof.com/programs/account-abstraction-bugs) | HackenProof | $1k – $250k | Yes | none | [eth-infinitism/account-abstraction repo, core + utils folders only, pinned tags v0.6.0-v0.9.0](https://github.com/eth-infinitism/account-abstraction) | 2026-11-19 |
| [Ethereum Foundation](https://ethereum.org/en/bug-bounty/) | Self-hosted | check program page | Unknown | none | [Ethereum protocol clients, consensus + execution layer, ethereum.org](https://github.com/ethereum) | 2026-11-20 |

## Gated — live, but filing costs something

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|

| [NEAR Intents — Smart Contracts](https://hackenproof.com/programs/near-intents-smart-contracts) | HackenProof | $100 – $300k | Unknown | $5/report | [NEAR Intents settlement contract (Rust)](https://github.com/defuse-protocol) | 2026-11-20 |
| [NEAR Intents — Bridges](https://hackenproof.com/programs/near-intents-bridges) | HackenProof | up to $300k | Unknown | $5/report | [NEAR Intents MPC + Omni Bridge](https://github.com/defuse-protocol) | 2026-11-20 |
| [Citrea](https://hackenproof.com/programs/citrea-protocol-and-smart-contracts) | HackenProof | $100 – $250k | Yes | $5/report | [Citrea rollup (Rust) + Clementine BitVM bridge](https://github.com/chainwayxyz) | 2026-11-20 |
| [Kamino](https://audits.sherlock.xyz/bug-bounties/433) | Sherlock | up to $1M | Yes | $250 USDC stake/report | [KLend, KVault, KFarms, Scope, Kamino Liquidity (Solana mainnet)](https://github.com/Kamino-Finance/klend) | 2026-11-19 |
| [Uniswap](https://cantina.xyz/bounties) | Cantina | up to $15.5M | Unknown | check program page | [Uniswap v4 core + periphery contracts, interfaces, wallets](https://github.com/Uniswap) | 2026-11-20 |
| [CoW Protocol](https://immunefi.com/bug-bounty/cowprotocol/information/) | Immunefi | up to $1M | Yes | Immunefi verification required to file | [CoW Protocol settlement contracts (Ethereum + Gnosis Chain), swap.cow.fi / cow.fi](https://github.com/cowprotocol/contracts) | 2026-11-20 |
| [Spark](https://immunefi.com/bug-bounty/sparklend/information/) | Immunefi | $50k – $5M | Unknown | Immunefi verification required to file | [Spark lending + savings (SparkLend, vaults, ALM), ~386 assets in scope](https://github.com/marsfoundation) | 2026-11-20 |
| [Metric](https://immunefi.com/bug-bounty/metric/information/) | Immunefi | up to $500k | Unknown | Immunefi verification required to file | [Check program page](https://immunefi.com/bug-bounty/metric/information/) | 2026-11-20 |
| [Paxos Labs](https://immunefi.com/bug-bounty/paxos-labs/information/) | Immunefi | $1k – $500k | Yes | Immunefi verification required to file | [Transit stablecoin conversion protocol + PAXGy tokenized gold (15 contracts)](https://immunefi.com/bug-bounty/paxos-labs/information/) | 2026-11-20 |
| [DAWN (USD.infra Vault)](https://immunefi.com/bug-bounty/dawn/information/) | Immunefi | $25k – $50k | Unknown | Immunefi verification required to file | [DAWN USD.infra Vault (Solana Anchor)](https://immunefi.com/bug-bounty/dawn/information/) | 2026-11-19 |
| [Folks Finance](https://immunefi.com/bug-bounty/folksfinance/information/) | Immunefi | up to $100k | Unknown | Immunefi verification required to file | [Check program page](https://immunefi.com/bug-bounty/folksfinance/information/) | 2026-11-19 |
| [OnRe](https://immunefi.com/bug-bounty/onre/information/) | Immunefi | up to $100k | Unknown | Immunefi verification required to file | [OnRe (Solana)](https://immunefi.com/bug-bounty/onre/information/) | 2026-11-19 |
| [RedStone](https://hackenproof.com/programs/redstone-smart-contracts) | HackenProof | $50 – $250k | Unknown | none | [RedStone oracle contracts (EVM Pull model + non-EVM chains)](https://github.com/redstone-finance) | 2026-11-19 |

## Closed / Paused

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|

| [Safe](https://docs.safefoundation.org/security/bug-bounty) | Self-hosted | up to $1M | Unknown | none | [Safe Smart Account contracts (v1.1.1-v1.5.0) + officially supported modules](https://github.com/safe-global/safe-smart-account) | 2026-11-20 |
| [Beanstalk](https://immunefi.com/bug-bounty/beanstalk/information/) | Immunefi | up to $1.1M | Unknown | Immunefi verification required to file | [Beanstalk stablecoin protocol, Basin, Beanstalk Farms](https://github.com/BeanstalkFarms/Beanstalk) | 2026-11-20 |
| [Scroll](https://r.xyz/bug-bounty/programs) | Remedy | up to $1M | Unknown | none | [Scroll bridge + rollup contracts (last known scope)](https://github.com/scroll-tech/scroll) | 2026-11-20 |

## Dead — do not trust aggregators that still list these

| Program | Platform | Reward range | KYC | Fee | Scope | Last verified |
|---|---|---|---|---|---|---|

| [Code4rena](https://code4rena.com) | Code4rena (audit contests) | check program page | Unknown | n/a | [n/a — platform wound down](https://code4rena.com) | 2026-11-19 |
| [Hats Finance](https://hats.finance) | Hats Finance | check program page | Unknown | n/a | [n/a — platform closed](https://hats.finance) | 2026-11-19 |

## Notes per program


### Across (active)

- **Platform:** Self-hosted
- **Program page:** https://docs.across.to/introduction/bug-bounty
- **Rewards:** Notice $0; Low $250; Medium $1,000; High $10,000; Critical up to $1,000,000.
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-19
- Only unprivileged loss/freeze findings with reproduction steps are eligible.

### Relay (active)

- **Platform:** Self-hosted
- **Program page:** https://docs.relay.link/security/bounties
- **Rewards:** Floor $500, cap $100,000. Severity x likelihood matrix with modifiers.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-19
- KYC + background check + tax docs required before payment (not before filing). Unprivileged exploit path only; Vaults out of scope.

### Marginfi (active)

- **Platform:** Self-hosted
- **Program page:** https://github.com/0dotxyz/marginfi-v2
- **Rewards:** Critical 2% of funds at risk (min $50,000, max $500,000); High $10,000-$50,000. Paid in USDC (Critical may be paid up to 80% in token if a token exists).
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-19
- Terms in the repo SECURITY.md. Long known-issues list in SECURITY.md doubles as a kill-filter — read it first.

### Venus (active)

- **Platform:** BNB Chain Bug Bounty (HackenProof partner program)
- **Program page:** https://bugbounty.bnbchain.org
- **Rewards:** P1 Critical $20,001-$100,000; P2 $5,001-$20,000; P3 $1,001-$5,000; P4 $300-$1,000; P* Extraordinary up to $150,000 case by case. Paid in BNB.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-19
- KYC before payout only. Fully discretionary program, no escrow; fully AI-generated reports are not accepted (policy section 4.3).

### ListaDAO (active)

- **Platform:** BNB Chain Bug Bounty (HackenProof partner program)
- **Program page:** https://bugbounty.bnbchain.org/scope-policy?project=1
- **Rewards:** Same BNB Chain tiers as Venus: P1 $20,001-$100,000; P4 floor $300; P* up to $150,000. Paid in BNB.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-19
- KYC before payout only. Fully AI-generated reports are not accepted (policy section 4.3).

### Valantis STEX (active)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs/valantis-stex
- **Rewards:** Critical up to $200,000; High up to $50,000. Medium/Low/Info NOT eligible. Paid in USDC/USD.
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-20
- Launched 23 Jul 2025, non-expiring. PoC required for all reports. 4 payouts recorded. kHYPEWithdrawalModule removed from scope 26 Jun 2026.

### Squads V4 (active)

- **Platform:** Self-hosted
- **Program page:** https://github.com/Squads-Protocol/v4
- **Rewards:** Steal Funds $300,000; Freeze Funds $200,000; Replay Attacks $25,000; Settings Modifications $10,000. Paid in 12-month locked SOL.
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-20
- Terms in the repo SECURITY.md. OFAC-sanctioned countries excluded. Single-program scope securing ~$10B.

### AUTOfinance (Tokemak) (active)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs/tokemak
- **Rewards:** Critical $25,000-$125,000 (capped at 10% of economic damage); High $25,000 flat. Medium/Low/Info NOT eligible. Paid in ETH, TOKE, or stablecoins.
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-20
- Active since 19 Sep 2024, non-expiring. 13 payouts recorded. PoC + fix suggestion required for all reports. Local forks only.

### UFarm Digital (active)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs/ufarm-digital
- **Rewards:** Critical $10,000-$100,000; High $1,000-$10,000; Medium $100-$1,000; Low up to $100. Paid in USDT.
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-20
- Active since 24 Feb 2025, non-expiring. 8 payouts recorded. v2 contracts relaunched 25 Aug 2026. High/Critical need a runnable PoC.

### BOB (active)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs/bob
- **Rewards:** Critical $10,000-$250,000 (10% of economic damage, min $10,000); High $2,000-$10,000; Medium $1,000-$2,000; Low up to $1,000. Paid in USDC.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-20
- KYC Required badge on the program page, but no timing stated anywhere in the public program text — confirm before hunting. Active since 16 Jul 2024. 1 payout recorded.

### Boba Network (active)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs/boba-network
- **Rewards:** Critical $10,000-$100,000 (10% of funds affected); High up to $8,000; Medium up to $3,000; Low up to $1,000. Paid in USDC.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-20
- KYC Required badge, timing unstated. Very narrow scope — all other Boba contracts are out. Active since 19 Apr 2024. 3 payouts recorded.

### PancakeSwap (active)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs/pancakeswap
- **Rewards:** Critical $20,000-$1,000,000 (5% of funds at risk; Group 1 core contracts min $50,000, Group 2 min $20,000); High up to $20,000. Medium/Low NOT eligible for smart contracts. Paid in CAKE.
- **KYC:** No · **Fee:** none
- **Last verified:** 2026-11-20
- 0 payouts recorded in ~2.5 years on Remedy — treat the headline max with caution. The same tiers are also published on the project's Immunefi program page.

### Arc (Circle) (active)

- **Platform:** HackerOne
- **Program page:** https://hackerone.com/arc-bbp
- **Rewards:** Extreme up to $1,000,000; Critical $20,000-$200,000.
- **KYC:** Unknown · **Fee:** none
- **Last verified:** 2026-11-19
- Launched Sep 2026. HackerOne Signal-gated — fresh accounts get only 3 shared trial reports; burning them without a triage means a 90-day pause. High report volume (4,765 reports/90d).

### Stellar (active)

- **Platform:** HackerOne
- **Program page:** https://hackerone.com/stellar
- **Rewards:** Standard tiers start at $0 (fully discretionary panel): Critical up to $25,000, High up to $15,000. Protocol carveout: Critical blockchain/DLT bugs pay 10% of funds affected, capped at $250,000. Paid in XLM.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-19
- KYC before payout only (full name, DOB, proof of address + tax forms). Consolidated onto HackerOne 7 May 2026; the old Immunefi program is deprecated. Only released/tagged code is eligible.

### Chainlink (active)

- **Platform:** HackerOne
- **Program page:** https://hackerone.com/chainlink
- **Rewards:** Top reward $100,000. Floor unverified (older reports cite $100 — check program page).
- **KYC:** Unknown · **Fee:** none
- **Last verified:** 2026-11-19
- Live since May 2019. CCIP is NOT on HackerOne — it is Immunefi-only. Same contracts pay up to $3M on Immunefi (verification-gated route).

### Anchor framework (active)

- **Platform:** Self-hosted
- **Program page:** https://github.com/arcium-hq/anchor
- **Rewards:** Critical 118-1,176 SOL; Medium 59-294 SOL; Low 1-59 SOL. Paid in 12-month locked SOL. USD figures approximate at ~$100/SOL (Oct-Nov 2026 reference).
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-19
- Terms in the repo SECURITY.md. KYC required before payout only. Repo moved from coral-xyz to arcium-hq (Arcium now maintains Anchor). Must be a bug in the framework itself, not user code.

### ERC-4337 Account Abstraction (active)

- **Platform:** HackenProof
- **Program page:** https://hackenproof.com/programs/account-abstraction-bugs
- **Rewards:** Critical up to $250,000; range $1,000-$250,000. No per-tier table in program text.
- **KYC:** Yes · **Fee:** none
- **Last verified:** 2026-11-19
- Run by the Ethereum Foundation (a distinct program from the main EF bounty). Mandatory KYC at payout. $73,000 paid to date. No reputation gate observed — the only HackenProof entry here with positive no-gate evidence.

### Ethereum Foundation (active)

- **Platform:** Self-hosted
- **Program page:** https://ethereum.org/en/bug-bounty/
- **Rewards:** Check program page for current tiers.
- **KYC:** Unknown · **Fee:** none
- **Last verified:** 2026-11-20
- The main EF program (protocol clients). Distinct from the ERC-4337 HackenProof program listed separately.

### NEAR Intents — Smart Contracts (gated)

- **Platform:** HackenProof
- **Program page:** https://hackenproof.com/programs/near-intents-smart-contracts
- **Rewards:** Critical $100,000-$300,000; High $20,000-$100,000; Medium $1,000-$20,000; Low $100-$1,000. High/Critical capped at 10% of funds at risk. $500,200 paid to date.
- **KYC:** Unknown · **Fee:** $5/report
- **Last verified:** 2026-11-20
- $5 submission fee per report. No reputation gate. Payout may be NEAR vested 1 year; payout KYC possible.

### NEAR Intents — Bridges (gated)

- **Platform:** HackenProof
- **Program page:** https://hackenproof.com/programs/near-intents-bridges
- **Rewards:** Headline Critical up to $300,000, but the program rules text caps Critical at $100,000 — the $300k figure is misleading. High $5,000-$10,000.
- **KYC:** Unknown · **Fee:** $5/report
- **Last verified:** 2026-11-20
- $5 submission fee per report. No reputation gate.

### Citrea (gated)

- **Platform:** HackenProof
- **Program page:** https://hackenproof.com/programs/citrea-protocol-and-smart-contracts
- **Rewards:** Critical $25,000-$250,000 (10% of funds, $25,000 floor); High $10,000-$25,000; Medium $1,000-$3,000; Low $100-$1,000. Paid in USDC on Ethereum.
- **KYC:** Yes · **Fee:** $5/report
- **Last verified:** 2026-11-20
- Triple gate — 50 HackenProof reputation points required + $5 submission fee + KYC required. 809 submissions vs $11,300 paid (strict triage).

### Kamino (gated)

- **Platform:** Sherlock
- **Program page:** https://audits.sherlock.xyz/bug-bounties/433
- **Rewards:** Theft 10% of funds at risk, cap $1,000,000; irreversible loss 5%, cap $100,000; temporary freeze discretionary, cap $10,000. No minimum payouts. No Medium/Low — only Critical/High submittable.
- **KYC:** Yes · **Fee:** $250 USDC stake/report
- **Last verified:** 2026-11-19
- $250 USDC stake per report (Polygon native USDC, refunded unless spam/AI/out-of-scope). KYC before payout only. PoC required. Live since 17 Oct 2026.

### Uniswap (gated)

- **Platform:** Cantina
- **Program page:** https://cantina.xyz/bounties
- **Rewards:** Critical up to $15,500,000; High up to $1,000,000; Medium up to $100,000; Low up to $50,000. Check program page for current tiers.
- **KYC:** Unknown · **Fee:** check program page
- **Last verified:** 2026-11-20
- Cantina charges per-report submission fees on most programs; a third-party aggregator (BountyOperator, Nov 2026) reports a $50 fee + KYC for Uniswap — unconfirmed, check the program page before filing. Launched 26 Nov 2024.

### CoW Protocol (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/cowprotocol/information/
- **Rewards:** Smart contracts Critical max $1,000,000; Websites/Apps Critical max $10,000. Paid in USDC on Ethereum. PoC required for all reports.
- **KYC:** Yes · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-20
- Immunefi-gated — filing requires platform verification (Human Passport or Skin in the Game). KYC required.

### Spark (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/sparklend/information/
- **Rewards:** Smart Contract Critical $50,000-$5,000,000 (10% of funds affected); High $10,000-$100,000. Paid in DAI on Ethereum.
- **KYC:** Unknown · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-20
- Immunefi-gated — filing requires platform verification. Live since 1 Nov 2023; program page last updated 13 Nov 2026. PoC required for Critical/High.

### Metric (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/metric/information/
- **Rewards:** Maximum bounty $500,000. Check program page for tier details.
- **KYC:** Unknown · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-20
- Immunefi-gated — filing requires platform verification. Launched 10 Nov 2026.

### Paxos Labs (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/paxos-labs/information/
- **Rewards:** Critical $10,000-$500,000 (10% of funds affected); High $5,000-$10,000; Medium $1,000. Paid in USDG on Ethereum.
- **KYC:** Yes · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-20
- Immunefi-gated — filing requires platform verification. KYC required. PoC required. Live since 20 Oct 2026.

### DAWN (USD.infra Vault) (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/dawn/information/
- **Rewards:** Critical $25,000-$50,000. Check program page for other tiers.
- **KYC:** Unknown · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-19
- Immunefi-gated — filing requires platform verification. Live since Jul 2026.

### Folks Finance (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/folksfinance/information/
- **Rewards:** Maximum bounty $100,000. Check program page for tier details.
- **KYC:** Unknown · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-19
- Immunefi-gated — filing requires platform verification. Program closes 31 Dec 2026.

### OnRe (gated)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/onre/information/
- **Rewards:** Maximum bounty $100,000. Check program page for tier details.
- **KYC:** Unknown · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-19
- Immunefi-gated — filing requires platform verification.

### RedStone (gated)

- **Platform:** HackenProof
- **Program page:** https://hackenproof.com/programs/redstone-smart-contracts
- **Rewards:** Critical $50,000-$250,000; High $10,000-$50,000; Medium $1,000-$10,000; Low $50-$1,000. Figures from secondary sources quoting the listing (reward table is JS-rendered).
- **KYC:** Unknown · **Fee:** none
- **Last verified:** 2026-11-19
- Effectively inaccessible to fresh accounts — 150 HackenProof reputation points required to file. $0 paid after 216 submissions (as of 18 Nov 2026). NOT dead — the program is live, the gate is the problem.

### Safe (closed)

- **Platform:** Self-hosted
- **Program page:** https://docs.safefoundation.org/security/bug-bounty
- **Rewards:** Rewards up to $1,000,000 depending on severity and impact. Paid in USDC on Ethereum.
- **KYC:** Unknown · **Fee:** none
- **Last verified:** 2026-11-20
- CLOSED until 2026-12-01 — re-check after that date. Program page itself was updated 2026-11-16 and still lists terms; do not file until reopening is confirmed.

### Beanstalk (paused)

- **Platform:** Immunefi
- **Program page:** https://immunefi.com/bug-bounty/beanstalk/information/
- **Rewards:** Maximum bounty $1,100,000 (when active).
- **KYC:** Unknown · **Fee:** Immunefi verification required to file
- **Last verified:** 2026-11-20
- PAUSED — not accepting reports (paused early Nov 2026). Immunefi vault holds $0. Live since 11 Oct 2022; page last updated 27 Oct 2026.

### Scroll (closed)

- **Platform:** Remedy
- **Program page:** https://r.xyz/bug-bounty/programs
- **Rewards:** Last known tiers before removal: Critical up to $1,000,000; High $10,000-$50,000; Medium $5,000.
- **KYC:** Unknown · **Fee:** none
- **Last verified:** 2026-11-20
- No longer on Remedy's public program list as of Nov 2026 — treat as closed; re-check the Remedy board before hunting.

### Code4rena (dead)

- **Platform:** Code4rena (audit contests)
- **Program page:** https://code4rena.com
- **Rewards:** n/a — platform dead.
- **KYC:** Unknown · **Fee:** n/a
- **Last verified:** 2026-11-19
- DEAD — wind-down announced 13 May 2026, last contest ended 27 May 2026. Customers migrated to Immunefi. Aggregators still list it active — do not trust them.

### Hats Finance (dead)

- **Platform:** Hats Finance
- **Program page:** https://hats.finance
- **Rewards:** n/a — platform dead.
- **KYC:** Unknown · **Fee:** n/a
- **Last verified:** 2026-11-19
- DEAD — hosted operations closed 31 Dec 2025. Aggregators still list it active — do not trust them.

---

_36 programs: 18 active, 13 gated, 3 closed/paused, 2 dead. Machine-readable source: [programs.yaml](programs.yaml). Link status: see [link-check-results.md](link-check-results.md)._
