import pytest

from backend.blockchain.block import Block, GENESIS_DATA

def test_mine_block():
    last_block = Block.genesis()
    data = 'test-data'
    block = Block.mine_block(last_block, data)

    assert isinstance(block, Block)
    assert block.data == data
    assert block.last_hash == last_block.hash

def test_genesis():
    genesis = Block.genesis()
    assert isinstance(genesis, Block)
    for key, value in GENESIS_DATA.items():
        assert getattr(genesis, key) == value

@pytest.fixture
def last_block():
	return Block.genesis()

@pytest.fixture
def block(last_block):
	return Block.mine_block(last_block, 'test_data')

def test_is_valid_block(last_block, block):
	Block.is_valid_block(last_block, block)


def test_is_valid_block_bad_last_hash(last_block, block):
	block.last_hash = 'evil_last_hash'

	with pytest.raises(Exception, match='last_hash must be correct'):
		Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_proof_of_work(last_block, block):
	block.hash = 'fff'

	with pytest.raises(Exception, match='proof of work requirement was not met'):
		Block.is_valid_block(last_block, block)

def test_is_valid_block_jumped_difficulty(last_block, block):
	jumped_difficulty = 10
	block.difficulty = jumped_difficulty
	block.hash = f'{"0" * jumped_difficulty}111abc'

	with pytest.raises(Exception, match='difficulty must only adjust by 1'):
		Block.is_valid_block(last_block, block)

def test_is_valid_block_bad_block_hash(last_block, block):
	block.hash = '0000000000000000bbbabc'

	with pytest.raises(Exception, match='block hash must be correct'):
		Block.is_valid_block(last_block, block)
